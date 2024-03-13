from django.forms import ModelForm
from .models import *


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "theme", "content"]


class CreateCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]