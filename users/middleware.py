'''
    Game plane [ TODO ]:
    - Check session validity if expired delete session and logout user 
    - else set request.user to user object and if there is no session set user to AnonymousUser object
'''

from django.contrib.auth.backends import BaseBackend
from django.utils import timezone
import pytz
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .mongodb import session_collection
from .helper import User

class AuthMiddleWare(BaseBackend):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def auth(self, request):
        pass

class SessionMiddleWare(BaseBackend):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.fill_session(request)
        return self.get_response(request)

    def get_session(self, sid):
        return session_collection().find_one({"sid": sid})

    def get_session_id(self, request):
        return request.COOKIES.get('sid')

    def delete_session(self, sid):
        session_collection().delete_one({'sid': sid})

    def fill_session(self, request):
        sid = self.get_session_id(request) or None
        ''''
            check session object for validity....
        '''
        session = self.get_session(sid)
        self.validate_session(request)
        if session is not None:
            ''' Make User Object for authenticated user functionality '''
            request.session = session
            request.user = User()


    def validate_session(self, request):
        sid = self.get_session_id(request) or None
        session = self.get_session(sid)

        if session is not None:
            exp = session.get('exp')
            utc = pytz.UTC
            if utc.localize(exp) < timezone.now():
                self.delete_session(sid)