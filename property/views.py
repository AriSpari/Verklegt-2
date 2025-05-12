from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from property.models import Property


def index(request):
    # TODO: Retrieve data from database
    db_properties = Property.objects.all()
    return render(request, "properties/properties.html", {
        "properties": db_properties
    })


# def get_property_by_id(request, id):
#     property = [x for x in properties if x['id'] == id]
#     return render(request, "properties/property_detail.html", {
#         "property": property
#     })

def get_property_by_id(request, id):
    property = get_object_or_404(Property, pk=id)
    # if not property:
    #     return HttpResponse("Property not found", status=404)
    return render(request, "properties/property_detail.html", {
        "property": property
    })

def get_property_by_name(request, name):
    return HttpResponse(f"Response from {request.path} with name {name}")

def user_profile(request):
    properties = Property.objects.all()  # query all properties from database
    return render(request, "user/profile.html", {
        "properties": properties
    })

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

