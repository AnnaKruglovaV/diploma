from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, CategoryDetailView, ProductListView, ProductDetailView, ContactsView, \
    HomeListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/product/', ProductListView.as_view(), name='product_list'),
    path('category/product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('', HomeListView.as_view(), name='home_list'),
]
