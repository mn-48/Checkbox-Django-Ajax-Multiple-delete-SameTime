from django.urls import path
from  .views import  Product_view, ProductC_create

urlpatterns = [
    path('', Product_view.as_view(), name='home'),
    path('create/', ProductC_create.as_view(), name='create'),
]
