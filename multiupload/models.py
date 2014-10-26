from django.db import models
import uuid, os

# Create your models here.
class Image(models.Model):
  img = models.ImageField(upload_to = "uploaded_img")
  name = models.CharField(max_length = 200)
  contentType = models.CharField(max_length = 200)
  imgHash = models.CharField(max_length = 17, unique = True)
  # Automatically set the field to 'now' when the object is created.
  dateAdded = models.DateField(auto_now_add = True)
   
   
  def __str__(self):
    return "%s" % (self.img.name)
   
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