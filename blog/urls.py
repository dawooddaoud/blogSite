from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'blog'

urlpatterns = [
    path('',views.PostList.as_view(),name='posts'),
    path('categories/',views.CategoryList.as_view(),name='categories'),
    path('<slug:slug>/',views.post_detail, name = 'post_detail'),
    path('category/<category>/', views.blog_category, name="blog_category"),
    path('post/upload/',views.PostCreate.as_view(), name='create'),
    path('post/<slug:slug>/edit/',views.PostUpdate.as_view(), name = 'update'),
    path('post/done/',views.done, name = 'done'),
    path('post/edited/',views.edited, name = 'edited'),
]
