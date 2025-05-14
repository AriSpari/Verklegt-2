# Modified views.py

from lib2to3.fixes.fix_input import context
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from offers.models import Offers
from property.models import Property
from offers.forms import OfferForm
from property.filters import PropertyFilter

def index(request):
    property_filter = PropertyFilter(request.GET, queryset=Property.objects.all())
    context = {
        'form': property_filter.form,
        'property': property_filter.qs,
    }

    db_properties = Property.objects.all()
    return render(request, "properties/properties.html", context)


def property_list(request):
    f = PropertyFilter(request.GET, queryset=Property.objects.all())

    city_val = request.GET.get("city", "")
    print("Filtering city with:", city_val)
    print("Matches:", Property.objects.filter(city__icontains=city_val).count())

    return render(request, 'properties/properties.html', {
        'properties': f.qs
    })

# This function can be removed or redirected to property_detail
def get_property_by_id(request, id):
    # Redirect to the main property_detail view to avoid duplication
    return property_detail(request, id)

def get_property_by_name(request, name):
    return HttpResponse(f"Response from {request.path} with name {name}")

def user_profile(request):
    properties = Property.objects.all()  # query all properties from database
    return render(request, "user/profile.html", {
        "properties": properties
    })


def submit_purchase_offer(request, id):
    property = Property.objects.get(id=id)  # Get the specific property by its ID
    return render(request, "submit_purchase_offer.html", {
        "property": property  # Pass the specific property to the template
    })

def confirm_offer(request, id):
    property_obj = get_object_or_404(Property, pk=id)
    offer_price = request.GET.get('offer_price')
    expire_date = request.GET.get('expire_date')

    return render(request, "properties/confirm_offer.html", {
        "property": property_obj,
        "offer_price": offer_price,
        "expire_date": expire_date
    })


def property_detail(request, id):
    property_obj = get_object_or_404(Property, pk=id)

    # Existing offer check
    existing_offer = None
    if request.user.is_authenticated:
        existing_offer = Offers.objects.filter(
            buyer_id=request.user,
            property_id=property_obj
        ).first()

    # Set button text - ensure this logic is correct
    button_text = "Update Offer" if existing_offer else "Submit Offer"

    # Form handling
    form = OfferForm()
    if existing_offer:
        form = OfferForm(initial={
            'offer_price': existing_offer.offer_price,
            'expire_date': existing_offer.expire_date,
        })

    # Debug print
    print(f"Button text determined as: {button_text}")

    context = {
        'property': property_obj,
        'form': form,
        'offers': Offers.objects.filter(property_id=property_obj),
        'existing_offer': existing_offer,  # Make sure existing_offer is passed to template
        'button_text': button_text,
    }
    return render(request, 'properties/property_detail.html', context)