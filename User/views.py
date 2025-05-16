from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from property.models import Property
from .forms import UserRegistrationForm, ProfileUpdateForm, SellerRegistrationForm


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
            messages.success(request, "Registration successful! Welcome to your new profile.")
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
            messages.success(request, "Your profile has been successfully updated!")
            return redirect('profile')  # reload so changes appear
        else:
            messages.error(request, "Please correct the errors below.")
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


@login_required
def become_seller(request):
    if request.user.is_seller:
        return redirect('profile')  # Already a seller, redirect to profile

    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_seller = True
            user.save()
            messages.success(request, "Congratulations! Your seller account has been activated.")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SellerRegistrationForm(instance=request.user)

    return render(request, 'User/become_seller.html', {
        'form': form,
    })