# Modified views.py

from lib2to3.fixes.fix_input import context
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from offers.models import Offers
from property.models import Property
from offers.forms import OfferForm
from property.filters import PropertyFilter
from User.models import User

def index(request):
    property_filter = PropertyFilter(request.GET, queryset=Property.objects.all())
    context = {
        'form': property_filter.form,
        'property': property_filter.qs,
    }

    db_properties = Property.objects.all()
    return render(request, "properties/properties.html", context)


def property_list(request):
    # Get the filter instance
    f = PropertyFilter(request.GET, queryset=Property.objects.all())

    # Get the sort parameter
    sort_by = request.GET.get('sort_by', '')

    # Apply sorting if specified
    queryset = f.qs
    if sort_by:
        if sort_by == 'price_asc':
            queryset = queryset.order_by('property_price')
        elif sort_by == 'price_desc':
            queryset = queryset.order_by('-property_price')
        elif sort_by == 'size_asc':
            queryset = queryset.order_by('squaremeters')
        elif sort_by == 'size_desc':
            queryset = queryset.order_by('-squaremeters')
        elif sort_by == 'date_asc':
            queryset = queryset.order_by('listing_date')
        elif sort_by == 'date_desc':
            queryset = queryset.order_by('-listing_date')

    return render(request, 'properties/properties.html', {
        'properties': queryset,
        'filter': f,
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


def seller_profile(request, seller_id):
    try:
        seller = get_object_or_404(User, user_id=seller_id)
        print(f"Found seller: {seller.username}")

        # Debug profile image
        if hasattr(seller, 'profile_image'):
            print(f"Profile image: {seller.profile_image}")
            if seller.profile_image:
                print(
                    f"Profile image URL: {seller.profile_image.url if hasattr(seller.profile_image, 'url') else 'No URL'}")
        else:
            print("Seller has no profile_image attribute")

        # Get the seller's properties
        seller_properties = Property.objects.filter(seller_id=seller)
        print(f"Found {seller_properties.count()} properties for this seller")

        return render(request, 'properties/seller_profile.html', {
            'seller': seller,
            'properties': seller_properties
        })
    except Exception as e:
        print(f"Error in seller_profile: {str(e)}")
        return HttpResponse(f"Error loading seller profile: {str(e)}")


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