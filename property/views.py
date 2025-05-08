from django.http import HttpResponse
from django.shortcuts import render

properties = [
    {
        "id": 1,
        "name": "Ari's house",
        "image": "https://www.bhg.com/thmb/H9VV9JNnKl-H1faFXnPlQfNprYw=/1799x0/filters:no_upscale():strip_icc()/white-modern-house-curved-patio-archway-c0a4a3b3-aa51b24d14d0464ea15d36e05aa85ac9.jpg",
        "address": "Aragata 4",
        "city": "Reykjavík",
        "postal_code": "101",
        "listing_price": 75000000,
        "description": "A bright modern home in a quiet neighborhood with a large patio and open floor plan.",
        "type": "Single-family",
        "room_count": 6,
        "bedroom_count": 3,
        "bathroom_count": 2,
        "is_sold": False,
        "listing_date": "2025-04-10",
        "square_meters": 145,
        "property_valuation": 72000000,
        "fire_insurance_value": 68000000
    },
    {
        "id": 2,
        "name": "Muggur's house",
        "image": "https://hips.hearstapps.com/hmg-prod/images/west-virginia-gray-cottage-64dd6bb056057.jpg?crop=0.943xw:0.817xh;0.0224xw,0.0932xh&resize=980:*",
        "address": "Muggastræti 20",
        "city": "Akureyri",
        "postal_code": "600",
        "listing_price": 58000000,
        "description": "Charming cottage with mountain views, perfect for peaceful living.",
        "type": "Cottage",
        "room_count": 5,
        "bedroom_count": 2,
        "bathroom_count": 1,
        "is_sold": True,
        "listing_date": "2025-03-22",
        "square_meters": 110,
        "property_valuation": 56000000,
        "fire_insurance_value": 53000000
    },
    {
        "id": 3,
        "name": "Nói's house",
        "image": "https://www.livehome3d.com/assets/img/articles/design-house/how-to-design-a-house.jpg",
        "address": "Nóabraut 69",
        "city": "Hafnarfjörður",
        "postal_code": "220",
        "listing_price": 91000000,
        "description": "Spacious home with modern amenities, a large garden, and close to schools.",
        "type": "Villa",
        "room_count": 8,
        "bedroom_count": 4,
        "bathroom_count": 3,
        "is_sold": False,
        "listing_date": "2025-02-28",
        "square_meters": 180,
        "property_valuation": 88000000,
        "fire_insurance_value": 85000000
    }
]



def index(request):
    #TODO: Retrieve data from database
    return render(request, "properties/properties.html", {
        "properties": properties
    })

# def get_property_by_id(request, id):
#     property = [x for x in properties if x['id'] == id]
#     return render(request, "properties/property_detail.html", {
#         "property": property
#     })

def get_property_by_id(request, id):
    property = next((x for x in properties if x['id'] == id), None)
    # if not property:
    #     return HttpResponse("Property not found", status=404)
    return render(request, "properties/property_detail.html", {
        "property": property
    })

def get_property_by_name(request, name):
    return HttpResponse(f"Response from {request.path} with name {name}")

def user_profile(request):
    return render(request, "user/profile.html", {
        "properties": properties #placeholder context
    })

def submit_purchase_offer(request,id):
    return render(request, "submit_purchase_offer.html",{
        "properties": properties #placeholder context
    })