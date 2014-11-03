"""
    AngularJS, Django, and Jquery File-upload App.
                Sandeep Jadoonanan
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.conf import settings
from django.views.generic import View
import os, json

from .models import Image


def handleUpload(request):
  # This view accepts only POST methods.
  if request.method == "POST":
    
    # Get the uploaded file.
    f = request.FILES["thefiles"]
    # Replace any whitespaces with underscores.
    f.name = Image.unscorize(f.name)
    
    # Instantiate an Image object with the uploaded file.
    imgFile = Image(img = f, name = f.name, contentType = f.content_type, imgHash = Image.getHash())
    imgFile.save()
    
    # Create a JSON response (for Jquery File Upload).
    res = {
      "files": []
    }
    res["files"].append(imgFile.toObj())
    
    jsonResponse = json.dumps(res)
    
    return HttpResponse(jsonResponse, content_type = "application/json")
    
  else:
    return HttpResponseBadRequest("Only POST requests are allowed!", content_type = "application/json")
   
  raise Http404


def handleDelete(request, hash):
  # Get Image object with the exact ImgHash as the paramater 'hash'.
  imgFile = get_object_or_404(Image, imgHash = hash)
  
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



# NOTE: Make this ONLY POST requests.
def returnImagesJSON(request):
  """
  Return JSON data for all objects loaded. This way,
  AngularJS can construct the template on the front-end for us.
  """
  # This view accepts only POST methods.
  if request.method == "POST":
     
    limit = 12
     
    ImageData = {
      "files": []
    }
    # Limit the results to 'x' amount of Images.
    for img in Image.objects.all()[:limit]:
      ImageData["files"].append(img.toObj(True))
     
    jsonResponse = json.dumps(ImageData)
     
    return HttpResponse(jsonResponse, content_type = "application/json")
   
  else:
    return HttpResponseBadRequest("Only POST requests are allowed!", content_type = "application/json")
   
  raise Http404
  