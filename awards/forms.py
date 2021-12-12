from .models import Projects,Votes,Comments,Profile
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['user','design','usability','content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user','pro_id']

class RateForm(forms.ModelForm):
    class Meta:
        model = Votes
        exclude = ['user','project']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']