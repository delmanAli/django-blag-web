from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user_name', 'user_email', 'text')
        locals = {
            'user_name': 'Name',
            'user_email': 'Email',
            'text': 'Your Comment'
        }
        # widgets = {
        #     'user_name': forms.TextInput(attrs={'class': 'for  m-control'}),
        #     'user_email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'text': forms.Textarea(attrs={'class': 'form-control'})
        # }
