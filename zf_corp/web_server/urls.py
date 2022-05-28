from django.urls import path
from . import views

# APP LEVEL URLS WILL BE WRITTEN HERE.
urlpatterns = [
    path('',views.index,name='serverIndex'),
    path('home/',views.home,name='serverHome'),
]

