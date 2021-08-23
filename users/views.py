from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Register view.
def register(request):
    form = UserCreationForm()
    return render (request, 'users/register.html',{'form': form})

