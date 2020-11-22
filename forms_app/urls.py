from django.urls import path

from forms_app.views import FormsListView, FormCreateView, FormUpdateView

urlpatterns = [
    path('', FormsListView.as_view(), name='forms_list'),
    path('create/', FormCreateView.as_view(), name='form_create'),
    path('edit/<slug>', FormUpdateView.as_view(), name='form_edit'),
]
