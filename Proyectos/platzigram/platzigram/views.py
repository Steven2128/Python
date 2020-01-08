from django.http import HttpResponse
from datetime import datetime


def say_hi(request, name, age):
    if age<18:
        message = "You wouldn't stay here"
    else:
        message = "Welcome"
    return HttpResponse("Hi, "+name+"!. "+message)


def hello_world(request):
    now = datetime.now().strftime("%dth %b %Y - %H:%M")
    return HttpResponse("Oh, hi. The time is "+str(now))