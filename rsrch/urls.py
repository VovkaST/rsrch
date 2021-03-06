"""rsrch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rsrch.views import IndexView


urlpatterns = [
    path('tinymce/', include('tinymce.urls')),

    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view()),
    path('admin/', admin.site.urls),
    path('forms/', include('forms_app.urls')),
    path('questionnaires/', include('questionnaire_app.urls')),
    path('results/', include('results_app.urls')),
    path('doc_tmpls/', include('doc_templates_app.urls')),
    path('end_pgs/', include('ending_pages_app.urls')),
]
