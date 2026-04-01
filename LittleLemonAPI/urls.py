from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

urlpatterns = [
    path('menu-items/', MenuItemListView.as_view(), name="menu-items"),
    path('bookings/', BookingListView.as_view(), name='bookings' ),
    path('bookings/<int:pk>', SingleBookingView.as_view(), name='bookings' ),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('msg/', msg),
    path('api-token-auth/', obtain_auth_token)
]