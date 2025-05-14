from django.urls import path
from . import views

app_name = 'offers'  # This is important for namespacing

urlpatterns = [
    path('make_offer/<int:property_id>/', views.make_offer, name='make_offer'),
    path('my-offers/', views.my_offers, name='my-offers'),
    path('make_offer/<int:property_id>/', views.make_offer, name='make_offer'),
]