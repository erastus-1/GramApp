from cloudinary.models import CloudinaryField
# from django.contrib.auth.models import User
from django.db import models
import cloudinary

# Create your models here.
class Profile(models.Model):
    profile_pic =CloudinaryField('image', blank=True) 
    bio = models.CharField(max_length=255)
    # owner = models.ManyToManyField(User,blank=True, on_delete=models.CASCADE, related_name="profile")

class Image(models.Model):
    pic=CloudinaryField(manual_crop='1080x800', blank=True)
    name= models.CharField(max_length=55)
    caption = models.TextField(blank=True)
    # profile= models.ForeignKey(User, blank=True,on_delete=models.CASCADE)
    profile_details = models.ForeignKey(Profile,on_delete=models.CASCADE)


class Comment(models.Model):
    image = models.ForeignKey(Image,blank=True, on_delete=models.CASCADE,related_name='comment')
    # comment_owner = models.ForeignKey(User, blank=True,on_delete=models.CASCADE)
    comment= models.TextField()
