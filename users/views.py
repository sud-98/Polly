from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterFrom
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created Successfully! Login Now')
            return redirect('login')
    else:
        form = UserRegisterFrom()
    return render(request, 'users/register.html', {'form': form})
