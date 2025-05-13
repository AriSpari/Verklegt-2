from django.urls import path
from . import views

# app_name = 'offers'  # This is important for namespacing

urlpatterns = [
    path('<int:property_id>/offer/', views.make_offer, name='make-offer'),
    path('my-offers/', views.my_offers,name='my-offers'),
]