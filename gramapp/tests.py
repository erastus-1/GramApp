from .models import Profile,Comment,Image
from django.test import TestCase
from django.contrib.auth.models import User

#Create your tests here.

class ProfileTestClass(TestCase):
    '''
    test class for Profile model
    '''
    def setUp(self):
        self.new_user = User(username='test', email='testing@gmail.com', password='5678')
        self.new_user.save()
        self.new_profile = Profile(photo='image.png', bio='testbio', user=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_method(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)
            
    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)==0)


class ImageTestClass(TestCase):
    """test class for Image model"""

    def setUp(self):

        self.user = User.objects.create_user("testuser", "anyUser")

        self.new_profile = Profile(profile_pic='https://unsplash.com/photos/2PODhmrvLik',bio="test bio",
                                     owner=self.user)
        self.new_profile.save()

        self.new_image = Image(pic='https://unsplash.com/photos/2PODhmrvLik',
                               caption="image", profile=self.new_profile)

    def test_instance_true(self):
        self.new_image.save()
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_image_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 1)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()



class CommentTestClass(TestCase):

    """Test class for Comment Model"""

    def setUp(self):
        self.new_user = User.objects.create_user("testuser", "anyUser")

        self.new_profile = Profile(profile_pic='https://unsplash.com/photos/2PODhmrvLik',
                                     bio="test bio",
                                     owner=self.new_user)
        self.new_profile.save()

        self.new_image = Image(pic='https://unsplash.com/photos/2PODhmrvLik',
                               caption="image", profile='',profile_details=self.new_user)
        self.new_image.save()

        self.new_comment = Comment(
            image=self.new_image, comment_owner=self.new_profile, comment="post")

    def test_instance_true(self):
        self.new_comment.save()
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_save_comment(self):
        self.new_comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) == 1)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()
        Comment.objects.all().delete()
