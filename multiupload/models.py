"""
    AngularJS, Django, and Jquery File-upload App.
                Sandeep Jadoonanan
"""

from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
import uuid, os


class Image(models.Model):
  """
  The default Image model. 
  """
  
  # The image file.
  img = models.ImageField(upload_to = "uploaded_img")
  # Name of the file.
  name = models.CharField(max_length = 200)
  # Content-type of the file.
  contentType = models.CharField(max_length = 200)
  # A randomly generated hash (used for deleting the Image).
  imgHash = models.CharField(max_length = 17, unique = True)
  # Automatically set the field to 'now' when the object is created.
  dateAdded = models.DateTimeField(auto_now_add = True)
  # Thumbnail for the picture.
  thumbnail = ImageSpecField(source = "img",
                             processors = [ResizeToFill(150, 150)],
                             format = "JPEG",
                             options = {"quality": 80})
  
   
   
  def __str__(self):
    return "%s" % (self.name)
   
   
  def toObj(self):
    """
    Get data for this Image in a standard Python dictionary.
    """
    obj = {}
    obj["name"] = Image.descorize(self.name)
    obj["size"] = Image.getSize(self.img.size)
    obj["url"] = self.img.url
    obj["thumbnailUrl"] = self.thumbnail.url
    obj["deleteUrl"] = "/delete/" + str(self.imgHash) + "/"
    obj["deleteType"] = "POST"
    obj["contentType"] = self.contentType
    # Sunday Oct 26, 2014 - 06:13:57 PM
    obj["dateAdded"] = self.dateAdded.strftime("%A %b %d, %Y - %I:%M:%S %p")
    
    return obj
   
   
  @staticmethod
  def getSize(amt):
    """
    This function takes a file size (in bytes) and converts
    the output into readable format. Supports file sizes in:
    'bytes', 'kb',  and 'mb'.
    """
    fmt = lambda x: "{:,}".format(x)
    fstr = lambda x, y: float("%.1f" % (x / float(y)))
    kb = 1024
    mb = (1024 * 1024)
     
    if amt >= mb:
      amt = fmt(fstr(amt, mb)) + " mb"
      return amt 
     
    if amt >= kb:
      amt = fmt(fstr(amt, kb)) + " kb"
      return amt
     
    return fmt(amt) + " bytes"
   
   
  @staticmethod
  def getHash():
    """
    Generate a unique hash value for the Image instance.
     
    Ex:
    str(uuid.uuid4())                        ==> '5996ccdc-b591-4c08-992b-08988df5dc9c'
    str(uuid.uuid4())[-17:]                  ==>                    '992b-08988df5dc9c'
    str(uuid.uuid4())[-17:].replace("-", "") ==>                     '992b08988df5dc9c'
    """
    return str(uuid.uuid4())[-17:].replace("-", "")
   
   
  @staticmethod
  def unscorize(s):
    """
    Takes a string and replaces all
    whitespaces with underscores.
    """
    return s.replace(" ", "_")
   
   
  @staticmethod
  def descorize(s):
    """
    Takes a string and replaces all
    underscores with whitespaces.
    """
    return s.replace("_", " ")
  
  
