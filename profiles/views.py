from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from stories.models import Story
from django.template import RequestContext
from forms import UserProfileEditForm

def view_profile(request, username):
    user = get_object_or_404(User, username=username)
    
    # Get a list of story names the person contributed to.
    stories = Story.objects.filter(fragment__author=user).distinct().order_by('name')
    
    context = RequestContext(request, {'profile_user': user, 'stories':stories})
    return render_to_response('profiles/view_user.html', context)
    #return HttpResponse("Hello, " + username)
    
@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile_view',
                                kwargs={'username':request.user.username}))
    else:
        form = UserProfileEditForm(instance=request.user)
    return render_to_response('profiles/profile_edit_form.html',
                        RequestContext(request, {'form':form}))



@login_required
def password_change(request, template_name='profiles/password_change_form.html',
                    post_change_redirect=None):
    if post_change_redirect is None:
        post_change_redirect = reverse('profile_password_done')
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(post_change_redirect)
    else:
        form = PasswordChangeForm(request.user)
    return render_to_response(template_name, {
        'form': form,
    }, context_instance=RequestContext(request))

