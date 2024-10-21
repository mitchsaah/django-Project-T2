from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Saves user
            return redirect('login')  # VAfter successful login
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})