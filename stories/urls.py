from django.conf.urls.defaults import *
from models import Story
import settings

# Generic views ---------------
urlpatterns = patterns('django.views.generic',
    (r'^/?$', 'list_detail.object_list',
        {
            'queryset': Story.objects.all(),
            'template_object_name': 'story',
            'extra_context': {"title": "Story List"},
        }
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
