from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='buyer-index'),
    path('<int:id>', views.get_buyer_by_id, name='buyer-by-id'),
    path('<str:name>', views.get_buyer_by_name, name='buyer-by-name'),
]

