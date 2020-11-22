import io
import os
from datetime import datetime
from uuid import uuid4
from wsgiref.util import FileWrapper

from django.core.mail import send_mail
from django.db.models import Prefetch
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.views import generic

from questionnaire_app.models import Questionnaires
from results_app.forms import TemplatedForm
from rsrch.functions import get_pdf_content, make_pdf, str_m5, fill_template
from results_app.models import Results


class ResultsListView(generic.ListView):
    model = Results
    template_name = 'results_app/results_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(filled_at__isnull=False)


class ResultsCreate(generic.CreateView):
    model = Results

    def get(self, request, *args, **kwargs):
        questionnaire_id = kwargs['q']
        questionnaire_template = Questionnaires.objects.get(id=questionnaire_id)
        result = Results()
        result.questionnaire = questionnaire_template
        result.form = questionnaire_template.form
        result.document = questionnaire_template.document
        result.ending_page = questionnaire_template.ending_page
        result.link_fill_out = uuid4()
        result.data = {}
        result.save()
        return HttpResponseRedirect(reverse('results_fill_out', kwargs={'link': result.link_fill_out}))


class ResultsView(generic.DetailView):
    template_name = 'results_app/results_view.html'
    model = Results

    def get_object(self, queryset=None):
        link = self.kwargs.get('link')
        queryset = self.get_queryset()
        obj = queryset.filter(link_view_ending=link)\
            .prefetch_related('document')\
            .prefetch_related('ending_page').first()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.object:
            raise Http404()
        template = self.object.ending_page.content
        data = self.object.data
        context.update({
            'page_content': fill_template(template=template, data=data),
        })
        return context


class ResultsFillOut(generic.UpdateView):
    model = Results
    template_name = 'results_app/results_fill_out.html'
    fields = ['data']

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.filled_at:
            raise Http404()
        return self.render_to_response(self.get_context_data())

    def get_form(self, form_class=None, data=None):
        fields_dict = self.object.form.form_fields
        return TemplatedForm(fields_list=fields_dict, data=data)

    def get_object(self, queryset=None):
        link = self.kwargs.get('link')
        queryset = self.get_queryset()
        obj = queryset.filter(link_fill_out=link).prefetch_related(
            Prefetch('questionnaire', queryset=Questionnaires.objects.select_related('document'))
        ).prefetch_related('form').first()
        return obj

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form(data=request.POST)
        if form.is_valid():
            self.object.user_email = form.cleaned_data.pop('user_email')
            self.object.data = form.cleaned_data
            self.object.filled_at = datetime.now()
            self.object.meta = {
                'REMOTE_ADDR': self.request.META.get('REMOTE_ADDR'),
                'HTTP_USER_AGENT': self.request.META.get('HTTP_USER_AGENT'),
            }
            self.object.data_hash = str_m5(string=str(form.cleaned_data))
            view_result_link = str_m5(string=self.object.link_fill_out + self.object.data_hash)
            self.object.link_view_ending = view_result_link
            self.object.save()

            doc_template = self.object.questionnaire.document.content
            pdf_content = get_pdf_content(
                document_template=doc_template, data=form.cleaned_data,
                ending_page_url=reverse('results_view', kwargs={'link': view_result_link})
            )
            make_pdf(content=pdf_content, filename=self.object.link_fill_out)

            send_mail(subject=self.object.questionnaire.title, from_email=EMAIL_HOST_USER, html_message=pdf_content,
                      recipient_list=[self.object.user_email], message=None)

            return HttpResponseRedirect(reverse('results_list'))
        return self.form_invalid(form=form)


class DownloadResultView(generic.View):
    def get(self, request, *args, **kwargs):
        link = kwargs.get('link')
        file_path = PDF_RESULTS_DIR / f'{link}.pdf'
        if not file_path.is_file():
            raise Http404()
        file_like = FileWrapper(filelike=io.FileIO(file_path))
        content_type = 'application/pdf'
        response = HttpResponse(file_like, content_type=content_type)
        response['Content-Disposition'] = f'attachment; filename={file_path.name}'
        response['Content-Length'] = os.path.getsize(file_path)
        return response
