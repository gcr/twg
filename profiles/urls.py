from django.conf.urls.defaults import *
import views

# Generic views ---------------
urlpatterns = patterns('',
    url(
        r'^(?P<username>[\w-]+)/?', views.view_profile,
        name='profile_view'
    ),
)

