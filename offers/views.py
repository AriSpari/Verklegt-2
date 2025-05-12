from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from property.models import Property
from .models import Offers
from .forms import OfferForm  # Make sure you have this created


@login_required
def make_offer(request, property_id):
    property = get_object_or_404(Property, pk=property_id)

    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.property = property
            offer.buyer = request.user
            offer.save()  # This should update the database
            messages.success(request, 'Your offer has been submitted!')
            return redirect('property-detail', pk=property_id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = OfferForm()

    return render(request, 'property_detail.html', {
        'property': property,
        'form': form,
    })