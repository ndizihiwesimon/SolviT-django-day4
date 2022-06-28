from django.forms import forms
from django.contrib.auth import get_user_model
from blog.models import Blog
User = get_user_model()


class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
