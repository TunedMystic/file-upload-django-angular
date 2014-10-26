from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.conf import settings
from django.shortcuts import get_object_or_404
import os, json
import uuid

from .models import Image

# Create your views here.
def handleUpload(request):
  # This view accepts only POST methods.
  if request.method == "POST":
    
    # Get the uploaded file.
    f = request.FILES["thefiles"]
    # Replace any whitespaces with underscores.
    f.name = f.name.replace(" ", "_")
    
    # Instantiate an Image object with the uploaded file.
    imgFile = Image(img = f, name = f.name, contentType = f.content_type, imgHash = Image.getHash())
    imgFile.save()
    
    # Create a JSON response (for Jquery File Upload).
    res = {}
    res["name"] = imgFile.name
    res["size"] = imgFile.img.size
    res["deleteType"] = "POST"
    res["url"] = imgFile.img.url
    res["thumbnailUrl"] = imgFile.img.url
    res["deleteUrl"] = "/delete/" + str(imgFile.imgHash) + "/"
    res = {
      "files": [res]
    };
    
    jsonResponse = json.dumps(res)
    print "\n\n"
    print json.dumps(res, indent = 2)
    print "\n\n"
    
    return HttpResponse(jsonResponse, content_type = "application/json")
    
  else:
    return HttpResponseBadRequest("Only POST requests man!!", content_type = "application/json")
   
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
  
  