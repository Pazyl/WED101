from django.urls import path
from api import views

urlpatterns = [
    path('products/', views.all_products),
    path('products/<int:id>/', views.one_product),
    path('categories/', views.all_categories),
    path('categories/<int:id>/', views.one_category),
    path('categories/<int:c_id>/products/', views.all_products_by_category),
]
