from django.urls import path
from platzigram import views as local_views



urlpatterns = [
    path('hello-world/', local_views.hello_world),
    path('<str:name>/<int:age>',local_views.say_hi)
]
