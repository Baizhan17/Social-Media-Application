from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from .import api
urlpatterns = [
    path('me/',api.me,name='me'),
    path('signup/', api.signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('friends/<uuid:pk>/', api.friends, name='friends'),
    path('editprofile/',api.reset_account,name='reset_account'),
    path('editpassword/',api.reset_password,name='reset_password'),
    path('friends/<uuid:pk>/request/', api.send_friend_request, name='send_friend_request'),
    path('friends/<uuid:pk>/<str:status>/', api.handle_req, name='handle_req'),
]