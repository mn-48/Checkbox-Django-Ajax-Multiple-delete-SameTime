from django.shortcuts import render, redirect

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


    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            product_ids = request.POST.getlist('id[]')
            for id in product_ids:
                product = Product.objects.get(pk=id)
                print(product)
                product.delete()

            return redirect('home')