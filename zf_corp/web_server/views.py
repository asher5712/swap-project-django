from django.shortcuts import redirect, render

# Create your views here.
def indexView(request):
    return redirect('home/')

def homeView(request):
    return render(request, 'web_server/index.html')

def aboutView(request):
    return render(request, 'web_server/about.html')

def contactView(request):
    return render(request, 'web_server/contact.html')

def faqView(request):
    return render(request, 'web_server/faq.html')

def loginView(request):
    return render(request, 'web_server/login.html')

def loggedinView(request):
    return redirect('/')

def logoutView(request):
    return redirect('/')

def signupView(request):
    return render(request, 'web_server/signup.html')

def signedupView(request):
    return redirect('/')