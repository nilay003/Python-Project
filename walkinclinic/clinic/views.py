# # from django.shortcuts import render

# # # Create your views here.
# # #api
# # from django.shortcuts import HttpResponse
# # from django.urls import reverse_lazy


# # from django.views import View
# # from django.shortcuts import redirect
# # from django.db import transaction
# # # from .forms import PositionForm

# from django.shortcuts import HttpResponse
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
# from django.urls import reverse_lazy
# from .models import user,doctor,patient,appointment,invoice,prescription,routinecheckup,questionnairefacility,answer,requestequipment,reporting,feedback,promo

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login

# from django.views import View
# from django.shortcuts import redirect
# from django.db import transaction




# class registration_form(CreateView):
#     model = user
#     fields = ['firstname', 'lastname', 'birthday','contactno','street','city','country','postalcode','username','email','password','usertype']
#     template_name =  'registration_form.html'
#     def get_success_url(self):
#         success_url = reverse_lazy('userlogin')





# from django.contrib.auth.forms import AuthenticationForm

# class userlogin(LoginView):
#     model = user
#     template_name = 'userlogin.html'
#     authentication_form = AuthenticationForm
#     def get_success_url(self):
#         success_url = reverse_lazy('sucess')  # Redirect to success URL after successful login


# class sucess(CreateView):
#     template_name = 'sucess.html'
#     def get_success_url(self):
#         success_url = reverse_lazy('sucess')  # Redirect to success URL after successful login





from django.shortcuts import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from .models import user

class registration_form(CreateView):
    model = user
    fields = ['firstname', 'lastname', 'birthday', 'contactno', 'street', 'city', 'country', 'postalcode', 'username', 'email', 'password', 'usertype']
    template_name =  'registration_form.html'
    
    def get_success_url(self):
        return reverse_lazy('userlogin')

# class userlogin(LoginView,LoginRequiredMixin):
#     model = user
#     template_name = 'userlogin.html'
#     authentication_form = AuthenticationForm
#     success_url = reverse_lazy('sucess')  # Redirect to success URL after successful login
class userlogin(LoginView):
    model = user
    template_name = 'userlogin.html'
    fields = ['username','password']
    authentication_form = AuthenticationForm
    def get_success_url(self):
        return reverse_lazy('sucess')




class sucess(CreateView):
    model = user
    fields = ['username']
    template_name = 'sucess.html'
    def get_success_url(self):
        return reverse_lazy('sucess')  # Redirect to success URL after successful registration
