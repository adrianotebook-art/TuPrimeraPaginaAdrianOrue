from django import forms
from .models import Author, Post, Comment


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        
class PostSearchForm(forms.Form):
    title = forms.CharField(label='Buscar por título', max_length=200)