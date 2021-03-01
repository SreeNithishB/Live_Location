from django.urls import path
from .views import location_views

urlpatterns = [
    path('', location_views, name='location_views'),
]
