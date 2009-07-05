from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User

def view_profile(request, username):
    return HttpResponse(username)
