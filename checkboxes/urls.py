from django.urls import path
from  .views import  Product_view

urlpatterns = [
    path('', Product_view.as_view(), name='home'),
]
