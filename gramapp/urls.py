from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('search/', views.search, name='search')
    url(r'^image/$', views.add_image, name='upload_image'),
    url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
    url(r'^follow/(?P<user_id>\d+)', views.follow, name = 'follow'),
    url(r'^unfollow/(?P<user_id>\d+)', views.unfollow, name='unfollow'),
    url(r'^like/(\d+)/$', views.like_images,name='like')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)