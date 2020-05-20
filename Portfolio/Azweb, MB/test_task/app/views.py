from django.shortcuts import render
from .models import User, Product
from .forms import UserForm, ProductForm

def index(request):
    userform = UserForm()
    productform = ProductForm()
    if request.method == "POST":
        if request.POST.get("cart") == "Add to cart" or request.POST.get("price") == "To raise the price":
            if request.POST.get("cart") == "Add to cart":
                product = Product()
                product.name = request.POST.get("name")
                product.price = request.POST.get("price")
                user_id, user_name = request.session.get('user')
                product.user = User.objects.get(id=user_id)
                product.save()
            else:
                user_id, user_name = request.session.get('user')
                for item in Product.objects.filter(user=user_id):
                    item.price += 1
                    item.save()
            total_number_products_user = len(Product.objects.filter(user=user_id))
            total_number_products_all = len(Product.objects.all())
            max_price = max([item.price for item in Product.objects.filter(user=user_id)])
            average_price = sum([item.price for item in Product.objects.all()]) / total_number_products_all
            sum_price = sum([item.price for item in Product.objects.filter(user=user_id)])
            sum_select_price = 0
            for item in Product.objects.all():
                if (item.user_id == user_id and len(item.name) > 3) or item.price > 50:
                    sum_select_price += item.price
            return render(request, "statistic.html", {"user": user_name, "tnpu": total_number_products_user,
                                                      "tnpa": total_number_products_all, "max_price": max_price,
                                                      "average_price": average_price, "sum_price": sum_price,
                                                      "sum_select_price": sum_select_price})
        else:
            user_name = request.POST.get("name")
            user_password = request.POST.get("password")
            user = User.objects.filter(name=user_name)
            if user:
                user = user[0]
                if user.password == user_password:
                    request.session['user'] = [user.id, user.name]
                    return render(request, "cart.html", {"form": productform, "user": user.name})

    return render(request, "login.html", {"form": userform})

