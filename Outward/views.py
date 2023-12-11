from django.shortcuts import render
from .models import LearnPost
import json
# Create your views here.
def index(request):
    f = open("admin.json", "r");
    data = json.load(f);
    if (LearnPost.objects.all().count() < 1):
        LearnPost.objects.create(**json["business"])
        LearnPost.objects.create(**json["software"])
        LearnPost.objects.create(**json["web-design"])
    posts = LearnPost.objects.all()
    f.close();
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