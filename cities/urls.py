from django.urls import path

from cities.views import *
from cities.views import CityDetailView, CityCreateView

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('add/', CityCreateView.as_view(), name='create')

]
