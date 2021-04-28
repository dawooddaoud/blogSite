from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import Comment,Author,Post,Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views import generic
# Create your views here.



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    model = Post


def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    return render(request, template_name, {'post': post})


class CategoryList(generic.ListView):
    model = Category


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

def done(request):
    template_name = 'blog/done.html'
    return render(request,template_name)

class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    fields = ('title','category','author','content',)
    prepopulated_fields = {'slug': ('title',),}
    success_url = reverse_lazy('blog:done')

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('title','content',)
    success_url = reverse_lazy('blog:edited')


@login_required

def edited(request):
    template_name = 'blog/edit.html'
    return render(request,template_name)
