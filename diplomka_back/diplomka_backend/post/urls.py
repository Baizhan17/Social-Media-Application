from django.urls import path,include
from . import api
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
# router = DefaultRouter()
# router.register("posts", api.PostViewSet, basename="posts")

urlpatterns = [
    path('',api.post_list,name='post_list'),
    #path('', include(router.urls)),
    path('trends/',api.get_trends,name='get_trends'),
    path('create/',api.add_post,name='post_create'),
    path('profile/<uuid:id>/',api.post_list_profile,name='post_list_profile'),
    path('<uuid:pk>/comment/',api.add_comment,name='add_comment'),
    path('<uuid:pk>/like/',api.like_post,name='post_like'),
    path('<uuid:pk>/',api.post_comments,name='post_comments'),
    path('<uuid:id>/',api.post_list_profile,name='post_list_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)