from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')