from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def create_account(request):
    if request.user.is_authenticated():
        # We're already logged in!
        return HttpResponseRedirect("/")
        
    if request.method == 'POST':
        # Form submitted
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
            
    else:
        # New form
        form = UserCreationForm()
        
    return render_to_response("registration/register.html", RequestContext(request, {
        'form': form,
    }))

