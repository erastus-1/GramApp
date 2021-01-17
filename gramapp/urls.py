from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('search/', views.search, name='search'),
    url('image/', views.add_image, name='upload_image'),
    url('newprofile/',views.profile,name ='profile'),
    url('showprofile/(?P<id>\d+)',views.display_profile,name = 'showprofile'),
    url('comment/(?P<image_id>\d+)', views.comment, name='comment'),
    url('follow/(?P<user_id>\d+)', views.follow, name = 'follow'),
    url('unfollow/(?P<user_id>\d+)', views.unfollow, name='unfollow'),
    url('like/(\d+)/$', views.like,name='like')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)