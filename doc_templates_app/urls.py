from django.urls import path

from doc_templates_app.views import DocTemplatesCreateView, DocTemplatesListView, DocTemplatesDetailView

urlpatterns = [
    path('', DocTemplatesListView.as_view(), name='doc_templates_list'),
    path('create/', DocTemplatesCreateView.as_view(), name='doc_templates_create'),
    path('view/<slug>/', DocTemplatesDetailView.as_view(), name='doc_templates_view'),
]
