from django import forms
from .models import Post, Media
from cities_light.models import City, Country
from smart_selects.form_fields import ChainedModelChoiceField


class CreatePostForm(forms.ModelForm):
    #password = forms.CharField(label='Password', widget=forms.PasswordInput)
    #local = ChainedModelChoiceField('users', 'CustomUser', 'country', 'country', True, False, False, False, False)
    class Meta:
        model = Post
        fields = ['id', 'user_id', 'category_id', 'date', 'plus',
        'minus', 'local', 'shop', 'description', 'price', 'currency']

class CreateMedia(forms.ModelForm):
    media = forms.FileField(label='media')

    class Meta:
        model = Media
        fields = ['media']