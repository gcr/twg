from django.conf.urls.defaults import *
import django.contrib.auth.views
import django.views.generic
import views

# Generic views ---------------
urlpatterns = patterns('',
    url(
        r'^changepassword/?$', views.password_change,
        name='profile_change_password'
    ),
    
    url(
        r'^changepassword/done/?$', 'django.views.generic.simple.direct_to_template',
        {'template':'profiles/password_change_done.html'},
        name='profile_password_done'
    ),
    
    url(
        r'^view/(?P<username>[\w\d-]+)/?$', views.view_profile,
        name='profile_view'
    ),
    
    url(
        r'^edit/?$', views.edit_profile,
        name='profile_edit'
    ),
    
)

