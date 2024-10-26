from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('catalog/', views.catalog, name = 'catalog'),
    path('product/<int:id>', views.product, name = 'product'),
]
