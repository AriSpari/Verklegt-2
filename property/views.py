from django.http import HttpResponse
from django.shortcuts import render

properties = [
    {
        "id": 1,
        "name": "Ari's house",
        "image": "https://www.bhg.com/thmb/H9VV9JNnKl-H1faFXnPlQfNprYw=/1799x0/filters:no_upscale():strip_icc()/white-modern-house-curved-patio-archway-c0a4a3b3-aa51b24d14d0464ea15d36e05aa85ac9.jpg"
    },
    {
        "id": 2,
        "name": "Muggur's house",
        "image": "https://hips.hearstapps.com/hmg-prod/images/west-virginia-gray-cottage-64dd6bb056057.jpg?crop=0.943xw:0.817xh;0.0224xw,0.0932xh&resize=980:*"
    },
    {
        "id": 3,
        "name": "Nói's house",
        "image": "https://www.livehome3d.com/assets/img/articles/design-house/how-to-design-a-house.jpg"
    }
]


def index(request):
    #TODO: Retrieve data from database
    return render(request, "properties/properties.html", {
        "properties": properties
    })

def get_property_by_id(request, id):
    property = [x for x in properties if x.id == id]
    return render(request, "properties/property_detail.html", {
        "property": property
    })

def get_property_by_name(request, name):
    return HttpResponse(f"Response from {request.path} with name {name}")