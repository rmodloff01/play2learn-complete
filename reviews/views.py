from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Review
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['review']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewListView(ListView):
    model = Review

class ReviewDetailView(DetailView):
    model = Review

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['review']

class ReviewDeleteView(UserPassesTestMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('reviews:list')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user