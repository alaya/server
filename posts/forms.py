from django import forms
from .models import Post
from cities_light.models import City, Country
from smart_selects.form_fields import ChainedModelChoiceField


class CreatePostForm(forms.ModelForm):
    #password = forms.CharField(label='Password', widget=forms.PasswordInput)
    #local = ChainedModelChoiceField('users', 'CustomUser', 'country', 'country', True, False, False, False, False)
    class Meta:
        model = Post
        fields = ('shop', 'description', 'price', 'currency')
