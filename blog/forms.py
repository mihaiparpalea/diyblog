from django import forms
from .models import Comment

class AddComment(forms.Form):
	content = forms.CharField(widget=forms.Textarea())


# class AddComment(forms.ModelForm):
# 	class Meta:
# 		model = Comment
# 		fields = ('content',)