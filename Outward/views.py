from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html");

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