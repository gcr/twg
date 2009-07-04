# Create your views here.
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import datetime
import forms
from models import Story

@login_required
def add_fragment(request, story_id):
    if request.method == "POST":
        frag_form = forms.AddFragmentForm(request.POST)
        if frag_form.is_valid():
            story = Story.objects.get(pk=story_id)
            story.add_fragment(frag_form.cleaned_data['fragment_text'], request.user)
            return HttpResponseRedirect(reverse('story_detail', kwargs={'object_id':story_id}))
    else:
        # Return a form page
        frag_form = forms.AddFragmentForm()
        
    return render_to_response("stories/add_story_fragment.html",
        RequestContext(request, {
            'form':frag_form,
            'story':Story.objects.get(pk=story_id),
        })
    )
    
@login_required
def create_new_story(request):
    if request.method == "POST":
        # They attempted to create a story
        story_form = forms.NewStoryForm(request.POST)
        frag_form = forms.AddFragmentForm(request.POST)
        if story_form.is_valid() and frag_form.is_valid():
            # Store the new story and the fragment
            story = Story(
                name = story_form.cleaned_data['story_name'],
                last_update_date = datetime.datetime.now()
            )
            story.save()
            story.add_fragment(frag_form.cleaned_data['fragment_text'], request.user)
            return HttpResponseRedirect(reverse('story_detail', kwargs={'object_id':story.id}))
    else:
        # Return a blank form page
        story_form = forms.NewStoryForm()
        frag_form = forms.AddFragmentForm()
        
    return render_to_response("stories/add_new_story.html",
        RequestContext(request, {
            'story_form':story_form,
            'frag_form':frag_form,
        })
    )
