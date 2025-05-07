from django.shortcuts import render, redirect
from User.form import UserRegistrationForm
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        print(1)
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # hash password
            user.save()
            login(request, user)  # log them in after registering
            return redirect('home')  # or redirect to dashboard
    else:
        form = UserRegistrationForm()
    return render(request, 'User/register.html', {
            'form': form})
