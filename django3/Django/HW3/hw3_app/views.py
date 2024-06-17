from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Client, Product
 

def index(request):
    return render(request, 'hw3_app/index.html')

def client_orders(request, client_id):
    client = Client.objects.get(pk=client_id)

    # За последние 7 дней
    last_7_days = timezone.now() - timedelta(days=7)
    client_orders_last_7_days = Product.objects.filter(order__client=client, order__order_date__gte=last_7_days).distinct()

    # За последние 30 дней
    last_30_days = timezone.now() - timedelta(days=30)
    client_orders_last_30_days = Product.objects.filter(order__client=client, order__order_date__gte=last_30_days).distinct()

    # За последние 365 дней
    last_365_days = timezone.now() - timedelta(days=365)
    client_orders_last_365_days = Product.objects.filter(order__client=client, order__order_date__gte=last_365_days).distinct()

    return render(request, 'hw3_app/client_orders.html', {
        'client_orders_last_7_days': client_orders_last_7_days,
        'client_orders_last_30_days': client_orders_last_30_days,
        'client_orders_last_365_days': client_orders_last_365_days,
    })
