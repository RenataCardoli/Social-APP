from django import forms
from .models import Post, Contact, Comments

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))

    class Meta:
        model = Post
        fields = ('title', 'content')
        
class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='', widget=forms.TextInput(attrs={'placeholder': 'Comment here....'}))
    class Meta:
        model = Comments
        fields = ('content',)