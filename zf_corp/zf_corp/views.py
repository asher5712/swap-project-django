from django.shortcuts import render, redirect

# THE PROJECT LEVEL VIEWS WILL BE WRITTEN HERE.
def index(request):
    return redirect('/server')