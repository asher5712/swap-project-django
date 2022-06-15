from django.urls import path
from . import views

# HOMEPAGE LEVEL views will be written here.

urlpatterns = [
    path('', views.landing_page, name='landing-page'),
    path('faq/', views.faq, name='faq'),
    path('terms/', views.terms_of_service, name='terms-of-service'),
    path('privacy/', views.privacy, name='privacy'),
    
]