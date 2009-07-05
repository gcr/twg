# Create your views here.
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import list_detail
import datetime
import forms
from models import Story
from utils import slugify

@login_required
def add_fragment(request, slug):
    if request.method == "POST":
        frag_form = forms.AddFragmentForm(request.POST)
        if frag_form.is_valid():
            story = get_object_or_404(Story, slug=slug)
            story.add_fragment(frag_form.cleaned_data['fragment_text'], request.user)
            return HttpResponseRedirect(reverse('story_detail', kwargs={'slug':slug}))
    else:
        # Return a form page
        frag_form = forms.AddFragmentForm()
        
    return render_to_response("stories/add_story_fragment.html",
        RequestContext(request, {
            'form':frag_form,
            'story':get_object_or_404(Story, slug=slug),
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
            # Give 'er a slug!
            story.slug = slugify(story.name, instance=story)
            story.save()
            story.add_fragment(frag_form.cleaned_data['fragment_text'], request.user)
            return HttpResponseRedirect(reverse('story_detail', kwargs={'slug':story.slug}))
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
    
    
def view_story_detail(request, slug):
    # Small generic view wrapper.
    story = get_object_or_404(Story, slug=slug)
    # Return all the authors that contributed to this story.
    # (An author's contributed to this story if they've authored a fragment that
    # references this story)
    authors = User.objects.filter(fragment__story=story).distinct().order_by('username')
    return list_detail.object_detail(request,
            slug=slug,
            slug_field='slug',
            queryset= Story.objects.all(),
            template_object_name='story',
            extra_context={
                'form':forms.AddFragmentForm,
                'authors':authors,
            },
    )

