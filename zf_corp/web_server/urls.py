from django.urls import path
from . import views

# APP LEVEL URLS WILL BE WRITTEN HERE.
urlpatterns = [
    path('',views.indexView,name='serverIndex'),
    path('home/',views.homeView,name='serverHome'),
    path('about/',views.aboutView,name='serverAbout'),
    path('contact/',views.contactView,name='serverContact'),
    path('faq/',views.faqView,name='serverFAQ'),
    path('login/',views.loginView,name='serverLogIn'),
    path('loggedin/',views.loggedinView,name='serverLoggedIn'),
    path('signup/',views.signupView,name='serverSignUp'),
    path('signedup/',views.signedupView,name='serverSignedUp'),

]

