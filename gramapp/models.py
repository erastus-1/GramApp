from friendship.models import Friend,Follow,Block
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils import timezone
from vote.models import VoteModel
from django.db import models
import datetime as dt
import cloudinary

# Create your models here.
class Profile(models.Model):
    profile_pic =CloudinaryField('image', blank=True) 
    bio = HTMLField(blank=True)
    owner = models.OneToOneField(User,blank=True, on_delete=models.CASCADE, related_name="profile")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.bio)


    def profile_save(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    @classmethod
    def update_bio(cls,id, bio):
        display_profile = cls.objects.filter(id = id).update(bio = bio,)
        return display_profile

    @classmethod
    def get_all_profiles(cl):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def update_bio(cls,id, bio):
        update_profile = cls.objects.filter(id = id).update(bio = bio,)
        return update_profile


class Image(models.Model):
    pic = CloudinaryField('image', blank=True)
    name= models.CharField(max_length=55)
    caption = models.CharField(max_length=500,blank=True)
    profile= models.ForeignKey(User, blank=True,on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(profile__pk=profile)
        return images

    class Meta:
        ordering = ['-date_uploaded']


class Comment(models.Model):
    image = models.ForeignKey(Image,blank=True, on_delete=models.CASCADE,related_name='comment')
    comment_owner = models.ForeignKey(User, blank=True,on_delete=models.CASCADE)
    comment=  models.CharField(max_length = 250, blank=True)
    posted = models.DateTimeField(auto_now_add=True)


    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_image_comments(cls, id):
        comments = Comment.objects.filter(image__pk=id)
        return comments

    def __str__(self):
        return str(self.comment)


class Likes(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def save_likes(self):
        self.save()

    def delete_like(self):
        self.delete()

    def count_likes(self):
        likes = self.likes.count()
        return likes

class Follow(models.Model):
    follower = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='follower')
    followee = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='followee')
    
    def save_follow(self):
        self.save()

    def delete_follow(self):
        self.delete()

    def __str__(self):
        return self.following
