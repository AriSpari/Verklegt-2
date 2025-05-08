from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='property-index'),
    path('property/<int:id>', views.get_property_by_id, name='property-by-id'),
    path('<str:name>', views.get_property_by_name, name='property-by-name'),
    path('user-profile/', views.user_profile, name='user-profile'),
    path('property/<int:id>/submit-purchase-offer/', views.submit_purchase_offer, name='submit-purchase-offer'),

]

