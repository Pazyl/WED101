from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import Http404

from api.models import Product
from api.models import Category


def all_products(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def one_product(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': 'product does not exists'})
        # raise Http404

    return JsonResponse(product.to_json())


def all_categories(request):
    categories = Category.objects.all()
    json_categories = [category.to_json() for category in categories]
    return JsonResponse(json_categories, safe=False)


def one_category(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': 'category does not exists'})
        # raise Http404

    return JsonResponse(category.to_json())


def all_products_by_category(request, c_id):
    try:
        category = Category.objects.get(id=c_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': 'category does not exists []'})

    products = Product.objects.filter(category_id=category.id)

    if products.__len__() == 0:
        return JsonResponse({'info': 'qazir bul [category] boyinsha  [products] JOOOQ'})
    else:
        json_products = [p.to_json() for p in products]
        return JsonResponse(json_products, safe=False)


