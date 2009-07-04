# Create your views here.
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from forms import AddFragmentForm
from models import Story

@login_required
def add_fragment(request, story_id):
    if request.method == "POST":
        frag_form = AddFragmentForm(request.POST)
        if frag_form.is_valid():
            story = Story.objects.get(pk=story_id)
            story.add_fragment(frag_form.cleaned_data['fragment_text'], request.user)
            return HttpResponseRedirect(reverse('story_detail', kwargs={'object_id':story_id}))
    else:
        # Return a form page
        frag_form = AddFragmentForm()
        
    return render_to_response("stories/add_story_fragment.html",
        RequestContext(request, {
            'form':frag_form,
#            'user':request.user,
            'story':Story.objects.get(pk=story_id),
        })
    )
