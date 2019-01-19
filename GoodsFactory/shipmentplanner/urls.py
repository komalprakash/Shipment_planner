from django.urls import path
from shipmentplanner import views

urlpatterns=[
  path('',views.FirstPageHandler, name="FirstPageHandler")
]
