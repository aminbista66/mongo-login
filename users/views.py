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



from urllib.parse import urlparse

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.shortcuts import resolve_url


class AccessMixin:
    """
    Abstract CBV mixin that gives access mixins the same customizable
    functionality.
    """

    login_url = "/login"
    permission_denied_message = ""
    raise_exception = False
    redirect_field_name = REDIRECT_FIELD_NAME

    def get_login_url(self):
        """
        Override this method to override the login_url attribute.
        """
        login_url = self.login_url or settings.LOGIN_URL
        if not login_url:
            raise ImproperlyConfigured(
                f"{self.__class__.__name__} is missing the login_url attribute. Define "
                f"{self.__class__.__name__}.login_url, settings.LOGIN_URL, or override "
                f"{self.__class__.__name__}.get_login_url()."
            )
        return str(login_url)

    def get_permission_denied_message(self):
        """
        Override this method to override the permission_denied_message attribute.
        """
        return self.permission_denied_message

    def get_redirect_field_name(self):
        """
        Override this method to override the redirect_field_name attribute.
        """
        return self.redirect_field_name

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            raise PermissionDenied(self.get_permission_denied_message())

        path = self.request.build_absolute_uri()
        resolved_login_url = resolve_url(self.get_login_url())
        # If the login url is the same scheme and net location then use the
        # path as the "next" url.
        login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
        current_scheme, current_netloc = urlparse(path)[:2]
        if (not login_scheme or login_scheme == current_scheme) and (
            not login_netloc or login_netloc == current_netloc
        ):
            path = self.request.get_full_path()
        return redirect_to_login(
            path,
            resolved_login_url,
            self.get_redirect_field_name(),
        )
        

class ProtectedView(generic.TemplateView):
    template_name = "protected/index.html"