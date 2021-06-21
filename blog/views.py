from django.shortcuts import render
from blog.models import Post, Category
from blog.owner import OwnerCreateView, OwnerUpdateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django_xhtml2pdf.views import PdfMixin
from django.views.generic.detail import DetailView
from django.db.models import Q


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    model = Post


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreate(OwnerCreateView):
    model = Post
    fields = ['title', 'category', 'slug', 'content']
    success_url = reverse_lazy('blog:done')


class PostUpdate(OwnerUpdateView):
    model = Post
    fields = ['title', 'category', 'slug', 'content']
    success_url = reverse_lazy('blog:edit')


class PostPDFView(PdfMixin, DetailView):
    model = Post
    template_name = 'blog/post_pdf.html'


class CategoryList(generic.ListView):
    model = Category


class SearchResultsView(generic.ListView):
    model = Post
    template_name = 'blog/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query, status=1)
            )
        return object_list
    # https://learndjango.com/tutorials/django-search-tutorial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context
    # https://stackoverflow.com/questions/37958554/django-class-based-view-access-context-data-from-get-queryset


def blog_category(request, category):
    posts = Post.objects.filter(
        category__name__contains=category,
        status=1
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog/blog_category.html", context)


@login_required
def author_panel(request):
    posts = Post.objects.filter(owner=request.user, status=1)
    owners = Post.objects.filter(owner=request.user, status=1)[:1]
    context = {
        "posts": posts,
        "owners": owners,
    }
    return render(request, "blog/author_panel.html", context)


@login_required
def author_panel_drafts(request):
    posts = Post.objects.filter(owner=request.user, status=0)
    owners = Post.objects.filter(owner=request.user)[:1]
    context = {
        "posts": posts,
        "owners": owners,
    }
    return render(request, "blog/author_panel_drafts.html", context)


@login_required
def done(request):
    template_name = 'blog/done.html'
    owners = Post.objects.filter(owner=request.user, status=1)[:1]
    context = {'owners': owners}
    return render(request, template_name, context)


@login_required
def edited(request):
    template_name = 'blog/edit.html'
    owners = Post.objects.filter(owner=request.user, status=1)[:1]
    context = {'owners': owners}
    return render(request, template_name, context)
