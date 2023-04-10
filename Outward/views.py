from django.shortcuts import render
from .models import LearnPost
# Create your views here.
def index(request):
    posts = LearnPost.objects.all()
    return render(request, "index.html", {'posts': posts});

def learn_web_design(request):
    return render(request, "learn-web-design.html");

def learn_software(request):
    return render(request, "learn-software.html");

def learn_business(request):
    return render(request, "learn-business.html");

def terms_of_use(request):
    return render(request, "terms-of-use.html");
    
def privacy_policy(request):
    return render(request, "privacy-policy.html");

def learn_archive(request):
    posts = LearnPost.objects.all()
    return render(request, "learn-archive.html", {'posts': posts});