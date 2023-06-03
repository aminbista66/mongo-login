'''
    Game plane [ TODO ]:
    - Check session validity if expired delete session and logout user 
    - else set request.user to user object and if there is no session set user to AnonymousUser object
'''


from django.contrib.auth.backends import BaseBackend


class AuthMiddleWare(BaseBackend):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def auth(self, request):
        pass
