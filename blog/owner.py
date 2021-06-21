from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post

# Refrence check dj4e-samples/myart/owner.py

class OwnerCreateView(LoginRequiredMixin, CreateView):
    # Saves the form instance, sets the current object for the view, and redirects to get_success_url().
    def form_valid(self, form):
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        owners = Post.objects.filter(owner = self.request.user,status=1)[:1]
        context['owners'] = owners
        return context

class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        owners = Post.objects.filter(owner = self.request.user,status=1)[:1]
        context['owners'] = owners
        return context
