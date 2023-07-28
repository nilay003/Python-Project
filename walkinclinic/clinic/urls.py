# from django.urls import path
# from .views import registration_form,userlogin,sucess
# # from django.contrib.auth.views import LogoutView

# urlpatterns = [
#     path('registration_form/', registration_form.as_view(), name='registarion_form'),
#     path('userlogin/', userlogin.as_view(), name='userlogin'),
#     path('sucess/', sucess.as_view(), name='sucess'),
# ]

# clinic/urls.py

from django.urls import path
from .views import registration_form, userlogin, sucess

urlpatterns = [
    path('registration_form/', registration_form.as_view(), name='registration_form'),
    path('userlogin/', userlogin.as_view(), name='userlogin'),
    path('sucess/', sucess.as_view(), name='sucess'),
]
