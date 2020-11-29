# app/forms.py

from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'name',
            'post',
        )
        labels = {
            'post': 'ニックネーム',
            'post': '投稿内容',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'ニックネームを入力してください...', 'class': 'uk-input', }),
            'post': forms.Textarea(attrs={'placeholder': 'なにか入力してください...', 'class': 'uk-textarea', }),
        }
