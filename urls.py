from django.conf.urls.defaults import *
import settings
import stories

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Generic views ---------------
urlpatterns = patterns('django.views.generic.simple',
    (r'^/?$', 'redirect_to', {'url': '/stories/'}),
)
# Custom views ---------------
urlpatterns += patterns('',
    # Example:
    # (r'^twg/', include('twg.foo.urls')),
    (r'^stories/', include('stories.urls')),
    
    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)

if settings.DEBUG:
    # Add some debug templates and static files.
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)', 'django.views.static.serve',
            {"document_root":"/home/michael/Projects/twg/static"}),
    )
