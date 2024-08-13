from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView

from catalog.models import Category, Product, Company, Account


# class HomeListView(ListView):
#     model = Home


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = Product.objects.all()[:5]
        return context


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(category=self.object)
        return context


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class SearchView(TemplateView):
    model = Product
    template_name = "catalog/search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        print(query)
        return Product.objects.filter(name__icontains=query)


class CompanyListView(ListView):
    model = Company


class AccountListView(ListView):
    model = Account


# def create_appointment(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         surname = request.POST.get('surname')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         appointment_date = request.POST.get('appointment_date')
#         appointment_time = request.POST.get('appointment_time')
#
#         appointment = Appointment(name=name, phone=phone, surname=surname, email=email,
#                                   appointment_date=appointment_date,
#                                   appointment_time=appointment_time)
#         appointment.save()
#
#         return redirect('catalog:account_list')
#
#     return render(request, 'catalog/account_list.html', {'create_appointment': create_appointment})


# def diagnostic_results(request, appointment_id):
#     diagnostic_results = DiagnosticResult.objects.filter(appointment_id=appointment_id)
#     return render(request, 'catalog/account_list.html', {'diagnostic_results': diagnostic_results})
