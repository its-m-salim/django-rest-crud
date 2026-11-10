from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def home(request):
    return render(request, 'home.html')


def get_tables(request):
    tables = Tables.objects.filter(is_active=True).order_by("number")
    count = Tables.objects.filter(is_active=True, status="free").count()

    return render(request, 'table_select.html', {"tables": tables, "count": count})


def create(request, t_id):
    table = get_object_or_404(Tables, pk=t_id)

    if table.status == "busy":
        return redirect("table")

    if request.method == "POST":
        Orders.objects.create(
            user_name=request.POST["name"],
            dish_id=request.POST["dish"],
            table=table,
        )

        table.status = "busy"
        table.save()

        return redirect("read")

    dishes = Dishes.objects.filter(is_active=True)
    return render(request, 'create.html', {"dishes": dishes, "table": table})


def read(request):
    orders = Orders.objects.all().order_by("-id")
    count = orders.count()

    return render(request, 'read.html', {"orders": orders, "count": count})


def update(request, id):
    order = get_object_or_404(Orders, pk=id)

    if request.method == "POST":
        old_table = order.table
        new_table = get_object_or_404(Tables, pk=request.POST["table"])

        order.user_name = request.POST["name"]
        order.dish_id = request.POST["dish"]
        order.table = new_table
        order.status = request.POST["status"]
        order.save()

        if old_table != new_table:
            old_table.status = "free"
            old_table.save()

        if order.status == "paid":
            new_table.status = "free"
        else:
            new_table.status = "busy"
        new_table.save()

        return redirect("read")

    context = {
        "order": order,
        "tables": list(Tables.objects.filter(status="free").order_by("number")) + [order.table],
        "dishes": Dishes.objects.filter(is_active=True),
        "statuses": Orders.ORDER_STATUS,
    }
    return render(request, 'update.html', context)


def delete(request, id):
    order = get_object_or_404(Orders, pk=id)

    if request.method == "POST":
        table = order.table
        order.delete()

        table.status = "free"
        table.save()

        return redirect("read")

    return render(request, 'delete.html', {"order": order})