from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='seller-index'),
    path('<int:id>', views.get_seller_by_id, name='seller-by-id'),
    path('<str:name>', views.get_seller_by_name, name='seller-by-name'),
]

