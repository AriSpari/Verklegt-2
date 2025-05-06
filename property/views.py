from django.http import HttpResponse
from django.shortcuts import render

properties = [
    {
        "id": 1,
        "name": "Ari's house",
    },
    {
        "id": 2,
        "name": "Muggur's house",
    },
    {
        "id": 3,
        "name": "Nói's house",
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