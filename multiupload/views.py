"""
    AngularJS, Django, and Jquery File-upload App.
                Sandeep Jadoonanan
"""

from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import View
import json

from .models import Image


class HandleUpload(View):
  """
  Handles photo uploads via the jQuery-file-upload plugin.
  """
  
  def _allowed_methods(self):
    return ["post"]
   
  def post(self, request):
    # Get the uploaded file.
    f = request.FILES["thefiles"]
    # Replace any whitespaces with underscores.
    f.name = Image.unscorize(f.name)
    
    # Instantiate an Image object with the uploaded file.
    imgFile = Image(img = f, name = f.name, contentType = f.content_type, imgHash = Image.getHash())
    imgFile.save()
    
    # Create a JSON response (for Jquery File Upload).
    res = {
      "files": [imgFile.toObj()]
    }
    jsonResponse = json.dumps(res)
    
    return HttpResponse(jsonResponse, content_type = "application/json")


class HandleDelete(View):
  """
  Deletes an image based on its hash value (imgHash).
  """
  
  def _allowed_methods(self):
    return ["post"]
  
  def post(self, request, *args, **kwargs):
    # Get the image hash from url (Return 0 if no hash is found).
    imageHash = kwargs.pop("hash", 0)
    
    if imageHash == 0:
      raise Http404
    
    # Get Image object with the exact ImgHash as the url paramater 'hash'.
    imgFile = get_object_or_404(Image, imgHash = imageHash)
    
    # Create a JSON response (for Jquery File Upload).
    res = {}
    res[imgFile.name] = True
    res = {
      "files": [res]
    }
    
    # Delete the image
    imgFile.delete()
    jsonResponse = json.dumps(res)
    
    return HttpResponse(jsonResponse, content_type = "application/json")


class ImagesJSON(View):
  """
  Return JSON data for all objects loaded. This way,
  AngularJS can construct the template on the front-end for us.
  """
  
  def _allowed_methods(self):
    return ["post"]
  
  def post(self, request, *args, **kwargs):
    # Limit the results to 'x' amount of Images.
    limit = 12
     
    ImageData = {
      "files": []
    }
    
    for img in Image.objects.all()[:limit]:
      ImageData["files"].append(img.toObj(True))
     
    jsonResponse = json.dumps(ImageData)
     
    return HttpResponse(jsonResponse, content_type = "application/json")
