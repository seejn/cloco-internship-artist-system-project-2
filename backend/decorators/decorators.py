from Token.models import Token
from django.http import JsonResponse
# auth token check

def api_view(method):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if request.method not in method:
                return JsonResponse({"message": "Method not allowed"}, status=405)
            return func(request, *args, **kwargs)
        return wrapper
    return decorator


def check_auth_token(request):
    try:
        token = request.headers.get("Authorization").split(" ")[1]
        # token = request.headers
        print("Authorization header", token)
        user_token = Token.objects.get(token=token)
        print("token", user_token)
        if user_token.is_token_expired():
            print("Token expired")
            return False            
    except Exception as e:
        print(f"Exception:", e)
        return False
    return user_token.user


def login_required(func):
    def wrapper(request, *args, **kwargs):
        
        if check_auth_token(request):
            return func(request, *args, **kwargs)

        return JsonResponse({"message": "Authorization Failed from login_requried"}, status=401)

    return wrapper