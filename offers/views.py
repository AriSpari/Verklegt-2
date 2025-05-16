# Modified offers/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from property.models import Property
from .models import Offers
from .forms import OfferForm
from django.views.decorators.http import require_POST
from django_countries import countries



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
            return redirect('property-by-id', id=property_id)
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
def accept_offer(request, offer_id):
    # Get the offer
    offer = get_object_or_404(Offers, pk=offer_id)
    property_obj = offer.property_id

    # Check if user is the seller of the property
    if request.user != property_obj.seller_id:
        messages.error(request, "You are not authorized to accept this offer.")
        return redirect('property-by-id', id=property_obj.property_id)

    # Update offer status to "Accepted"
    offer.status_id = 2
    offer.save()

    messages.success(request, f"You have accepted the offer of {offer.offer_price} kr from {offer.buyer_id.username}.")

    return redirect('property-by-id', id=property_obj.property_id)

@login_required
def my_offers(request):
    offers = Offers.objects.filter(buyer_id=request.user)

    return render(request, 'offers/my_offers.html', {
        'offers': offers,
    })


@login_required
def finalize_offer(request, offer_id):
    # Always fetch the offer (and ensure it belongs to you)
    offer = get_object_or_404(Offers, pk=offer_id, buyer_id=request.user)
    property_obj = offer.property_id  # the related Property

    # Check if the offer status is "Accepted" (status_id 2)
    if offer.status_id != 2:  # Update this ID based on your Status table
        messages.error(request, "This offer has not been accepted by the seller yet.")
        return redirect('offers:my-offers')

    if request.method == 'POST':
        # Mark the property as sold
        property_obj.is_sold = True
        property_obj.save()

        # Update offer status to "Finalized" (status_id 5)
        offer.status_id = 5  # Update this ID based on your Status table
        offer.save()

        messages.success(request, "Congratulations! Your purchase has been finalized.")
        # Redirect to home
        return redirect('property_index')

    # GET → render the same multi-step review form
    return render(request, 'offers/finalize_offer.html', {
        'existing_offer': offer,
        'countries': countries  # Add countries to context
    })