from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from stories.models import Story
from django.template import RequestContext

def view_profile(request, username):
    user = get_object_or_404(User, username=username)
    
    # Get a list of story names the person contributed to.
    stories = Story.objects.filter(fragment__author=user).distinct().order_by('name')
    
    context = RequestContext(request, {'profile_user': user, 'stories':stories})
    return render_to_response('profiles/view_user.html', context)
    #return HttpResponse("Hello, " + username)
