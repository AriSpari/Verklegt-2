# Modified offers/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from property.models import Property
from .models import Offers
from .forms import OfferForm


@login_required
def make_offer(request, property_id):
    property_obj = get_object_or_404(Property, pk=property_id)

    # Check if user already has an offer for this property
    existing_offer = Offers.objects.filter(
        buyer_id=request.user,
        property_id=property_obj
    ).first()

    # Set button_text based on whether an offer exists
    button_text = "Update Offer" if existing_offer else "Submit Offer"

    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            if existing_offer:
                # Debugging - Check the data being submitted
                print(f"Existing offer found: {existing_offer.offer_id}")

                # Update existing offer
                existing_offer.offer_price = form.cleaned_data['offer_price']
                existing_offer.expire_date = form.cleaned_data['expire_date']
                existing_offer.save()
                messages.success(request, 'Your offer has been updated!')
            else:
                # Create new offer
                print("Creating new offer")
                offer = form.save(commit=False)
                offer.property_id = property_obj
                offer.buyer_id = request.user
                offer.save()
                messages.success(request, 'Your offer has been submitted!')

            # Redirect to property details page
            return redirect('property_detail', id=property_id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        # Pre-fill form with existing offer data if it exists
        if existing_offer:
            form = OfferForm(initial={
                'offer_price': existing_offer.offer_price,
                'expire_date': existing_offer.expire_date,
            })
        else:
            form = OfferForm()

    # Get all offers for this property to display in template
    offers = Offers.objects.filter(property_id=property_obj)

    # Return to property detail page with form and offers
    context = {
        'property': property_obj,
        'form': form,
        'offers': offers,
        'existing_offer': existing_offer,
        'button_text': button_text,  # Explicitly pass button text
    }

    # For debugging
    print(f"make_offer view button_text: {button_text}")

    return render(request, 'properties/property_detail.html', context)



@login_required
def my_offers(request):
    offers = Offers.objects.filter(buyer_id=request.user)
    properties = Property.objects.all()
    return render(request, 'offers/my_offers.html', {
        'offers': offers
    })