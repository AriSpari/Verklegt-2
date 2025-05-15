from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.property_list, name='property-list'),
    path('property/<int:id>', views.get_property_by_id, name='property-by-id'),
    path('<str:name>', views.get_property_by_name, name='property-by-name'),
    path('user-profile/', views.user_profile, name='user-profile'),
    # path('property/<int:id>/submit-purchase-offer/', views.submit_purchase_offer, name='submit-purchase-offer'),
    path('property/<int:id>/confirm-offer/', views.confirm_offer, name='confirm-offer'),
    path('toggle-favorite/<int:property_id>/', views.toggle_favorite, name='toggle-favorite'),
    path('favorites/', views.my_favorites, name='my-favorites'),
    path('', views.index, name='property_index'),
    path('property/<int:id>/', views.get_property_by_id, name='property_detail'),
    path('seller/<int:seller_id>/', views.seller_profile, name='seller-profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

