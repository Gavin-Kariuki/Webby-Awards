from django.shortcuts import render,redirect
from .models import Projects, Votes, Comments, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect, JsonResponse

# Create your views here.
def home_page(request):
    try:
        mradi = Projects.objects.all()
    except Exception as e:
        raise Http404()
    return render(request,"index.html",{"projects": mradi}) #mradi is the same as project
