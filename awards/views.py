from django.shortcuts import render,redirect
from .models import Projects, Votes, Comments, Profile
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect, JsonResponse

# Create your views here.
