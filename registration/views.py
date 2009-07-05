from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

def create_account(request):
    if request.user.is_authenticated():
        # We're already logged in!
        return HttpResponseRedirect("/")
        
    if request.method == 'POST':
        # Form submitted
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse("profile_edit"))
            
    else:
        # New form
        form = UserCreationForm()
        
    return render_to_response("registration/register.html", RequestContext(request, {
        'form': form,
    }))

