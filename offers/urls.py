from django.urls import path
from . import views

app_name = 'offers'  # This is important for namespacing

urlpatterns = [

    # path('<int:property_id>/confirm/', views.confirm_offer, name='confirm-offer')
    path('<int:property_id>/offer/', views.make_offer, name='make_offer'),

]