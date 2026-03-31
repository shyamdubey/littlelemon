from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

urlpatterns = [
    path('menu-items/', MenuItemListView.as_view()),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('msg/', msg),
    path('api-token-auth/', obtain_auth_token)
]