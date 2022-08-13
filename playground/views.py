from asyncio.windows_events import NULL
import collections
from genericpath import exists
from itertools import product
from math import prod
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db.models import Q
from store.models import Collection, Customer, Order, OrderItem, Product




def say_hello(request):

    queryset = Product.objects.filter(Q(inventory__lt=10)) | ~Q(unit_price__lt=20)
    

    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
