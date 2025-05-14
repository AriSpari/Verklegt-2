from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from property.models import Property




from .forms import UserRegistrationForm, ProfileUpdateForm


def register(request):
    """
    Display and process the sign-up form. Allows new users to set
    username, password, name—and optionally upload a profile image.
    On success, log them in and redirect to their profile page.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('profile')
    else:
        form = UserRegistrationForm()

    return render(request, 'User/register.html', {
        'form': form,
    })


@login_required
def profile(request):
    """
    Show the logged-in user's profile, and allow them to update their
    profile information including name, username, and profile image.
    """
    user = request.user

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # reload so changes appear
    else:
        form = ProfileUpdateForm(instance=user)

    return render(request, 'User/profile.html', {
        'user': user,
        'form': form,
    })
@login_required
def my_listings(request):
    listings = Property.objects.filter(seller_id=request.user)
    return render(request, 'user/my_listings.html', {
        'listings': listings
    })