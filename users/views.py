from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .helper import create_user_object, authenticate
from .mongodb import user_collection, session_collection
from django.utils import timezone
import uuid

class LoginView(generic.View):
    def get(self, *args, **kwargs):
        
        return render(self.request, 'users/login.html', {})

    def login(self, user):
        '''
            TODO: 
            - Create session for user (already created we need to populate the session)
            - store session in mongo db
            - send session_id to frontend as a cookie
        '''
        session_object = {
            'sid': str(uuid.uuid4().hex),
            'user_id': user.get('id'),
            'exp': timezone.now()
        }
        session_col = session_collection()
        session = session_col.find_one({"user_id": session_object.get('user_id')})
        if session is None:
            session_col.insert_one(session_object)
            return session_object['sid']
        return session.get('sid')

    def post(self, *args, **kwargs):
        post_object = {
            'email': '',
            'password': '',
        }
        
        for i in post_object.keys():
            post_object[i] = self.request.POST.get(str(i))
        user = authenticate(post_object['email'], post_object['password'])
        sid = self.login(user)
        response = HttpResponseRedirect(reverse_lazy('users:protected'))
        response.set_cookie('sid', sid, httponly=True)
        return response

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
            user_collection().insert_one(user_object)
        except Exception as e:
            raise e
        return HttpResponseRedirect(reverse_lazy('users:login'))

from django.contrib.auth.mixins import LoginRequiredMixin

class ProtectedView(LoginRequiredMixin, generic.View):
    template_name = "protected/index.html"

    def get(self, *args, **kwargs):
        print(self.request.user.is_authenticated())
        return render(self.request, self.template_name, {})