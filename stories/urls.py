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
        }
    ),
    
    # Individual story
    url(r'^(?P<object_id>\d+)/$', 'list_detail.object_detail',
        {
            'queryset': Story.objects.all(),
            'template_object_name': 'story',
            'extra_context': {'form':forms.AddFragmentForm},
        },
        'story_detail' # URL name
    ),
    
)

# Custom views ---------------
urlpatterns += patterns('',
    # Add a story
    url(r'^(?P<story_id>\d+)/add/?$', views.add_fragment, name='story_add_fragment')
)

