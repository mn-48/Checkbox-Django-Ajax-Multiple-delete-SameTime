from django.shortcuts import render

# Create your views here.
from  django.views.generic import  View
from .models import Product

class  Product_view(View):
    def get(self, request):
        allproduct = Product.objects.all()

        context = {
            'products':allproduct

        }

        return render(request, 'home.html', context)
        # return render(request, 'index.html', context)