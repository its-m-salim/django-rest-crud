from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import*

def home(request):
    return render(request, 'home.html')


def create(request):

    if request.method == "POST":
        order = Orders.objects.create(
            user_name = request.POST["name"],
            # dish_id = request.POST["dish"],
            table_id = request.POST["table"]
        )

        order.dish.set([request.POST["dish"]])

        return redirect("home")
    tables = Tables.objects.all()
    dishes = Dishes.objects.all()
    return render(request, 'create.html', {"tables": tables, "dishes": dishes})



def read(request):
    orders = Orders.objects.all()
    count = Orders.objects.count()
    return render(request, 'read.html', {"orders": orders, "count": count})