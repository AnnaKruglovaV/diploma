from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView

from catalog.models import Category, Product, Home


class HomeListView(ListView):
    model = Home


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Product.objects.all()[:5]
        return context


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=self.object)
        return context


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
