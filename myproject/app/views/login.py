from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpResponse

def user_login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            HttpResponseRedirect()
        else:
           return  httpresponse("<p>user authenticated. But unable to login. Check account</p>")
    else:
            #account does not exist. Hence redirect to account creation page
            HttpResponseRedirect()
        
           
             
