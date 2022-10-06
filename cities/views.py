from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView

from cities.forms import HtmlForm, CityForm
from cities.models import City

__all__ = (
    'home',
    'City',
    'CityDetailView',
    'CityCreateView',
    'CityDeleteView',
    'CityUpdateView',

)


def home(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            form.save()

    # if pk:
    #    city = get_object_or_404(City, id=pk)
    #    context = {'object': city}
    #    return render(request, "cities/detail.html", context)
    form = CityForm()

    qs = City.objects.all()
    paginator = Paginator(qs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'form': form}
    return render(request, "cities/home.html", context)


# class CityListView(ListView):
#     paginate_by = 3
#     model = City
#     template_name = 'cities/home.html'


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = "cities/detail.html"


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')


class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')


class CityUpdateView(UpdateView):
    model = City
    fields = ['name']
    template_name = 'cities/update.html'
    template_name_suffix = 'cities:home'
