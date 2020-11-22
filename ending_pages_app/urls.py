from django.urls import path

from ending_pages_app.views import (
    EndingPagesCreateView, EndingPagesListView, EndingPagesUpdateView
)


urlpatterns = [
    path('', EndingPagesListView.as_view(), name='ending_pages_list'),
    path('create/', EndingPagesCreateView.as_view(), name='ending_page_create'),
    path('edit/<slug>/', EndingPagesUpdateView.as_view(), name='ending_page_edit'),
]
