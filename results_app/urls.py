from django.urls import path

from results_app.views import (
    DownloadResultView, ResultsCreate, ResultsFillOut, ResultsListView, ResultsView
)

urlpatterns = [
    path('', ResultsListView.as_view(), name='results_list'),
    path('create/<int:q>/', ResultsCreate.as_view(), name='results_create'),
    path('view/<str:link>/', ResultsView.as_view(), name='results_view'),
    path('fillout/<str:link>/', ResultsFillOut.as_view(), name='results_fill_out'),
    path('download/<str:link>/', DownloadResultView.as_view(), name='results_download'),
]
