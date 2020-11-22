from django.urls import path

from ending_pages_app.views import EndingPagesListView, EndingPagesDetailView, EndingPagesCreateView

urlpatterns = [
    path('', EndingPagesListView.as_view(), name='ending_pages_list'),
    path('create/', EndingPagesCreateView.as_view(), name='ending_page_create'),
    path('view/<slug>/', EndingPagesDetailView.as_view(), name='ending_page_view'),
]
