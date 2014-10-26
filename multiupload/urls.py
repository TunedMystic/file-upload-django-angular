from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from . import views

urlpatterns = patterns("",
  
  url(r"^$", TemplateView.as_view(template_name = "multiupload/form.html")),
  url(r"^upload/$", views.handleUpload, name = "upload"),
  url(r"^delete/(?P<hash>\w+)/$", views.handleDelete, name = "delete"),
  
)