from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response

# register por medio del form en django normal
from .models import User
from django.views.generic.edit import FormView
from .forms import UserRegisterFrom

# register en DRF
from rest_framework.views import APIView
from rest_framework import status
from apps.users.api.serializers import UsersLoginSerializer, UserSignupSerializer, UserModelSerializer

#django normal
class UserCreate(FormView):
    template_name = 'users/register.html'
    success_url = '/'
    form_class = UserRegisterFrom


    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            #extra fields
            pais = form.cleaned_data['pais'],
        )
        return super(UserCreate, self).form_valid(form)




    # micreoservicio
# 
# class UsersLoginAPIView(APIView):
# 
#     def post(self, request, *args, **kwargs):     
#         serializer = UsersLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user, token = serializer.save()
#         data = {
#             'user': 'ok',
#             'token': token
#         }
#         return Response(data, status=status.HTTP_201_CREATED)
# 
class UserSignupAPIView(APIView):

    def post(self, request, *args, **kwargs):     
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)