import re
from django import forms
from django.contrib.auth.models import User
from MovieLib.models import Movie, Contact
#from MovieLib.models import Movie, Contact, Custmer
from django.utils.translation import ugettext_lazy as _

class MovieCreate(object):
    model = Movie
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Movie'})
        return kwargs


class MovieMixin(object):
    model = Movie
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Movie'})
        return kwargs

class UserContact(object):
    model = Contact
    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Contact'})
        return kwargs

'''class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)))
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Custmer
'''
#class RegistrationForm(forms.ModelForm):
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
       # fields = "__all__" 
        fields = ["username", "email", "password", "date_joined"] 
                              
'''class RegistrationForm(forms.Form):
    #model = Custmer
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

'''



