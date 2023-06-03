'''
    Game plane [ TODO ]:
    - Check session validity if expired delete session and logout user 
    - else set request.user to user object and if there is no session set user to AnonymousUser object
'''


from django.contrib.auth.backends import BaseBackend
from .mongodb import session_collection
from django.contrib.auth.models import AnonymousUser
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
        self.check_session(request)
        return self.get_response(request)

    def get_session(self, sid):
        return session_collection().find_one({"sid": sid})

    def check_session(self, request):
        sid = request.COOKIES.get('sid') or None
        ''''
            check session object for validity....
        '''
        session = self.get_session(sid)
        if session is not None:
            ''' Make User Object for authenticated user functionality '''
            request.user = User()