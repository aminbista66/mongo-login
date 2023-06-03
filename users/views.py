from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .helper import create_user_object, UserMixin, authenticate
from .mongodb import user_collection

class LoginView(generic.View):
    def get(self, *args, **kwargs):
        return render(self.request, 'users/login.html', {})

    def login(self, user):
        pass

    def post(self, *args, **kwargs):
        post_object = {
            'email': '',
            'password': '',
        }

        for i in post_object.keys():
            post_object[i] = self.request.POST.get(str(i))
        user = authenticate(post_object['email'], post_object['password'])
        
        return HttpResponseRedirect(reverse_lazy('users:protected'))

class RegisterView(generic.View):
    def get(self, *args, **kwargs):
        return render(self.request, 'users/register.html', {})

    def post(self, *args, **kwargs):
        post_object = {
            'email': '',
            'password': '',
            'confirm-password': ''
        }

        for i in post_object.keys():
            post_object[i] = self.request.POST.get(str(i))

        # contains hashed password
        user_object = create_user_object(post_object)

        try:
            user_collection.insert_one(user_object)
        except Exception as e:
            raise e
        return HttpResponseRedirect(reverse_lazy('users:login'))

class ProtectedView(generic.TemplateView):
    template_name = "protected/index.html"