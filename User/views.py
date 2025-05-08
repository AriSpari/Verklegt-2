from django.shortcuts import render, redirect
from User.form import UserRegistrationForm
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, user)  # log them in after registering
            return redirect('login')  # or redirect to dashboard
    else:
        form = UserRegistrationForm()
    return render(request, 'User/register.html', {
            'form': form})

def profile(request):
    return render(request, 'user/profile.html')
