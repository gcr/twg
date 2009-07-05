from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UserProfileEditForm(UserChangeForm):
    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email')
#    first_name = forms.CharField(
#        label="First name:",
#    )
#    
#    last_name = forms.CharField(
#        label="Last name:",
#    )
#    
#    email = forms.EmailField(
#        label="Email:",
#    )
