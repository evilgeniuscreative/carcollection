# context_processors.py
def logged_in(request):
    if request.user.is_authenticated:
       logged_in = True
    else:
        logged_in = False
    return {
        'logged_in' : logged_in 
    }