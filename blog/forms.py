from django import forms

from .models import Post

class PostForm(forms.ModelForm):
	"""docstring for PostForm"""
	class Meta:
		model = Post
		fields = ('title', 'text',)
			
ß
