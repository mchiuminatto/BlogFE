from django.shortcuts import render
# Create your views here.

import requests

def index(request):

    return render(request, "index.html")

def blog(request):
    posts = requests.get("http://localhost:8000/")
    j_posts = posts.json()
    # for p in j_posts:
    #     print(type(p))
    context = {'posts':j_posts}
    return render(request, "blog.html", context)