"""advbench_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from json.tool import main
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from MainApp.views import Upload, Predict #, VueView, send_file, send_js
from django.views.static import serve
from django.http import FileResponse

urlpatterns = [
    path('', TemplateView.as_view(template_name = "index.html")),
    path('/', TemplateView.as_view(template_name = "index.html")),
    path('/index.html', TemplateView.as_view(template_name = "index.html")),
    path('admin/', admin.site.urls),
    re_path(r"^upload?$", Upload.as_view()),
    re_path(r"^predict?$", Predict.as_view()),
    
    # static("css", document_root='../advbench_frontend/dist/css'),
    # static("js", document_root='../advbench_frontend/dist/js'),
    # path('favicon.ico', send_file, {'filename': '../advbench_frontend/dist/favicon.ico'}),
    # path('css/<path:path>', serve, {'document_root': '../advbench_frontend/dist/css'}),
    # path('js/<path:path>', serve, {'document_root': '../advbench_frontend/dist/js'}),
    # re_path(r'^js/(?*)$', send_js),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
