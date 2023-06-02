from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .helper import create_user_object
from .mongodb import get_db, user_collection, user

class LoginView(generic.View):
    def get(self, *args, **kwargs):
        return render(self.request, 'users/login.html', {})

class RegisterView(generic.View):
    def get(self, *args, **kwargs):
        print(user)
        return render(self.request, 'users/register.html', {})

    def post(self, *args, **kwargs):
        post_object = {
            'email': '',
            'password': '',
            'confirm-password': ''
        }

        for i in post_object.keys():
            post_object[i] = self.request.POST.get(str(i))
        user_object = create_user_object(post_object)
        
        return HttpResponseRedirect(reverse_lazy('users:login'))