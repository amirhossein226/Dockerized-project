from django import forms
from .models import Comment

# form for sharing posts by sending email


class PostShareForm(forms.Form):
    name = forms.CharField(max_length=50, label="نام")
    email = forms.EmailField(label="ایمیل فرستنده")
    recipient = forms.EmailField(label='ایمیل گیرنده')
    comment = forms.CharField(
        widget=forms.Textarea,
        required=False,
        label="توضیحات اضافه"
    )


# comment form which will be appear in detail.html and post_comment.html
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['author_name', 'author_email', 'body']
