from django import forms   # Forms import kortesi
from django.contrib.auth.models import User # Forms import kortesi
from django.contrib.auth.forms import UserCreationForm  # Forms import kortesi

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # form a email field thake na. sheta add korlam
    
    class Meta:
        model = User    # table name = USER
        fields = ['username','email','password1','password2']   # ei serially dekhabe form er moddhe
        