from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('product/<int:id>/', views.ProductView.as_view(), name='product'),
    path('add/', views.AddProduct.as_view(), name='add'),
    path('update/<int:id>/', views.UpdateProduct.as_view(), name='update'),
    path('delete/<int:id>/', views.DeleteProduct.as_view(), name='delete'),
]
