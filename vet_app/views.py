from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView
from vet_app.models import Category, Page


class IndexView(ListView):
    model = Category
    template_name = 'vet_app/index.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'home'
        return context


class PageView(DetailView):
    model = Page
    template_name = 'vet_app/page.html'
    context_object_name = 'page'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['menu'] = self.kwargs['cat']
        return context

    def get_queryset(self):
        get_object_or_404(Category, slug=self.kwargs['cat'])
        return super().get_queryset()


class CategoryView(PageView):

    def get_queryset(self):
        self.kwargs['cat'] = self.kwargs['slug']
        return super().get_queryset()


class StaffView(IndexView):
    template_name = 'vet_app/staff.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'staff'
        return context


class StrutturaView(IndexView):
    template_name = 'vet_app/struttura.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'struttura'
        return context


class DoveSiamoView(IndexView):
    template_name = 'vet_app/dove-siamo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'dove-siamo'
        return context


class ContattiView(IndexView):
    template_name = 'vet_app/contatti.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'contatti'
        return context