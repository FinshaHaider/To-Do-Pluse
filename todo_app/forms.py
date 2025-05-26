from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Notes


class TaskForm(forms.Form):
    task = forms.CharField(max_length=100)
    priority = forms.IntegerField(min_value=1, max_value=10)
    deadline = forms.DateField()

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']
    def username(self):
        username=self.cleaned_data['username']
        if len(username)<5:
            raise forms.ValidationError('Username should be at least 5 characters long')
        if not username.isalnum():
            raise forms.ValidationError('Username should only contain alphanumeric characters')
        if User.objects.filter(username=username).exist():
            raise forms.ValidationError('Username already exists. Please choose another')
        return username
    
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mt-3 mb-3'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mt-3 mb-3'}))
    
class NoteForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title','content']
        
    