from django.conf.urls.defaults import *
import views

# Generic views ---------------
urlpatterns = patterns('',
    url(
        r'^(?P<username>[\w\d-]+)/?$', views.view_profile,
        name='profile_view'
    ),
    
    url(
        r'^edit/(?P<username>[\w\d-]+)/?$', views.edit_profile,
        name='profile_edit'
    ),
)

