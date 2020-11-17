from django.urls import path

from forms_app.views import FormsListView, FormCreateView, FormDetailView

urlpatterns = [
    path('', FormsListView.as_view(), name='forms_list'),
    path('create/', FormCreateView.as_view(), name='form_create'),
    path('<slug>', FormDetailView.as_view(), name='form_view'),
]
