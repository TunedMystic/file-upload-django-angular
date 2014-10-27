from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from . import views

urlpatterns = patterns("",
  
  # The default index view, which is a file upload form.
  url(r"^$", TemplateView.as_view(template_name = "multiupload/form.html"), name = "form"),
  
  # Display all the Images at once.
  url(r"^view/$", TemplateView.as_view(template_name = "multiupload/view.html"), name = "view"),
  
  # Upload a picture.
  url(r"^upload/$", views.handleUpload, name = "upload"),
  
  # Delete a picture.
  url(r"^delete/(?P<hash>\w+)/$", views.handleDelete, name = "delete"),
  
  # Get JSON info for all Images.
  url(r"^93ec8e6b7a146f7d/$", views.returnImagesJSON, name = "ImagesJSON"),
  
)