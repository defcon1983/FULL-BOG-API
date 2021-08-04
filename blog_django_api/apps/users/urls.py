
# from .views import UserCreate, UserCreateAPIView


from .views import UserSignupAPIView, UserCreate

from django.urls import re_path


app_name = 'user_apps'

urlpatterns = [
    re_path('signup/', UserSignupAPIView.as_view(), name='signup'),
    re_path('signup-normal/', UserCreate.as_view(), name='signup-normal'),
]


