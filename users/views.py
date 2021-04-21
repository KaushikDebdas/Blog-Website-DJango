from django.shortcuts import render

# User form import
#from django.contrib.auth.forms import UserCreationForm

#nijer banano form
from .forms import UserRegisterForm

# message library import
from django.contrib import messages

#redirectin
from django.shortcuts import redirect

#login kora thaklei jate shudhu matro Profile show kore..otherwise profile show korbe na.
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    #form = UserCreationForm()
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #save the form in admin panel 
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account {username} successfully created')
            return redirect('blog-home')   
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()  # Register Form
    return render(request, 'users/register.html', {'form': form}) 


@login_required
def profile(request):
    return render(request, 'users/profile.html')