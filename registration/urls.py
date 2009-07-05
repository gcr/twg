from django.conf.urls.defaults import *
import settings
import views

# Generic views ---------------
urlpatterns = patterns('',
    url(r'^new_account/?$', views.create_account, name='register_new_account'),
)
