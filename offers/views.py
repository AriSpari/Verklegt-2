# offers/views.py


from django.shortcuts import render, redirect, get_object_or_404


from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from property.models import Property
from .models import Offers
from .forms import OfferForm

@login_required
def make_offer(request, property_id):
    property_obj = get_object_or_404(Property, pk=property_id)

    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.property_id = property_obj
            offer.buyer_id = request.user
            offer.save()
            messages.success(request, 'Your offer has been submitted!')
            return redirect('property_detail', id=property_id)
        messages.error(request, 'Please correct the errors below.')
    else:
        form = OfferForm()

    # Re-render the same detail template on GET or invalid POST
    offers = Offers.objects.filter(property_id=property_obj)
    return render(request, 'properties/property_detail.html', {
        'property': property_obj,
        'form': form,
    })


@login_required
def my_offers(request):
    offers = Offers.objects.filter(user=request.user)
    return render(request, 'offers/my_offers.html', {
        'offers': offers
    })


