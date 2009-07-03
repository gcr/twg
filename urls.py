from django.conf.urls.defaults import *
import settings
import stories
import django_openid_auth.forms

from django.contrib import admin
admin.autodiscover()

# Generic views ---------------
urlpatterns = patterns('django.views.generic.simple',
    (r'^/?$', 'redirect_to', {'url': '/stories/'}),
)

# Included apps ---------------
urlpatterns += patterns('',
    # Example:
    # (r'^twg/', include('twg.foo.urls')),
    (r'^stories/', include('twg.stories.urls')),
    
    (r'^admin/(.*)', admin.site.root),
    (r'^registration/', include('twg.registration.urls')),
    
    (r'^openid/', include('django_openid_auth.urls'), {'template_name': 'registration/login.html'}),
)

# User account management ---------------
urlpatterns += patterns('django.contrib.auth',
    url(r'^accounts/login/?', 'views.login', name='account_login'),
    #url(r'^logout/', views.logout, {'next_page': '/'}, 'accounts_logout'),
    url(r'^accounts/logout/?', 'views.logout_then_login', name='account_logout'),
)

if settings.DEBUG:
    # Add some debug templates and static files.
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)', 'django.views.static.serve',
            {"document_root":settings.MEDIA_URL}),
    )
