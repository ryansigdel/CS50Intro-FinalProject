from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Post,Comment


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']


class MakePost(ModelForm):
    class Meta:
        model = Post
        fields = ['name','photo','description']
		
		
       
class Comments(ModelForm):
	class Meta:
		model = Comment
		fields = ('name','body')
		widgets = {
			'name': forms.TextInput(attrs={'placeholder':'name'}) ,
			'body': forms.TextInput(attrs={'placeholder':'comment...',
			'id':'body','class':'form-control',
			'autocomplete':'off',
			}),
		}
        