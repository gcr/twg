from django.conf.urls.defaults import *
from models import Story
import views
import forms
import settings

# Generic views ---------------
urlpatterns = patterns('django.views.generic',
    # List of stories
    (r'^/?$', 'list_detail.object_list',
        {
            'queryset': Story.objects.all(),
            'template_object_name': 'story',
            # Allow people to create a new story inline
            'extra_context': {
                'story_form': forms.NewStoryForm,
                'frag_form': forms.AddFragmentForm,
            },
        }
    ),
    
    # Individual story
    url(r'^(?P<slug>[\w-]+)/$', 'list_detail.object_detail',
        {
            'slug_field':'slug',
            'queryset': Story.objects.all(),
            'template_object_name': 'story',
            'extra_context': {'form':forms.AddFragmentForm},
        },
        'story_detail' # URL name
    ),
    
)

# Custom views ---------------
urlpatterns += patterns('',
    # Add a fragment to a story
    url(r'^(?P<slug>[\w-]+)/add/?$', views.add_fragment, name='story_add_fragment'),
    
    # Add a story
    url(r'^new/?$', views.create_new_story, name='story_create_new'),
)

