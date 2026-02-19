from django.shortcuts import render
from django.views import generic

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Aplicativo
from .forms import AplicativoModelForm


class HomePageTemplateView(generic.TemplateView):
    template_name = 'hub/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aplicativos'] = Aplicativo.objects.filter(ativo=True)
        return context


class AplicativoCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'projetos/post.html'
    model = Aplicativo
    form_class = AplicativoModelForm
    success_url = reverse_lazy('pages:home')


class AplicativoUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'projetos/post.html'
    model = Aplicativo
    form_class = AplicativoModelForm


class AplicativoDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Aplicativo
    success_url = reverse_lazy('pages:home')