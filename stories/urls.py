from django.conf.urls.defaults import *
import settings

# Generic views ---------------
urlpatterns = patterns('django.views.generic',
    (r'^/?$', 'simple.direct_to_template',
        {
            'template': 'index.html',
#            'extra_context': {"title": "Welcome!"},
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
