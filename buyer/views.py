from django.http import HttpResponse

def index(request):
    return HttpResponse(f"Response from {request.path}")

def get_buyer_by_id(request):
    return HttpResponse(f"Response from {request.path}")

def get_buyer_by_name(request):
    return HttpResponse(f"Response from {request.path}")