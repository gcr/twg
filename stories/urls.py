from django.conf.urls.defaults import *
from models import Story
import settings

# Generic views ---------------
urlpatterns = patterns('django.views.generic',
    # List of stories
    (r'^/?$', 'list_detail.object_list',
        {
            'queryset': Story.objects.all(),
            'template_object_name': 'story',
            'extra_context': {"title": "Story List"},
        }
    ),
    
    # Individual story
    url(r'^(?P<object_id>\d+)/$', 'list_detail.object_detail',
        {
            'queryset': Story.objects.all(),
            'template_object_name': 'story',
        },
        'story_detail' # URL name
    ),
    
)

# Custom views ---------------
urlpatterns += patterns('',
    # Example:
    # (r'^twg/', include('twg.foo.urls')),
    
)

if settings.DEBUG:
    # Add some debug templates and static files.
    urlpatterns += patterns('',
        #(r'^delay_test/', stories.views.delay_test),
    )
