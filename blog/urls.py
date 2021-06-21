from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'blog'

urlpatterns = [
    path('',views.PostList.as_view(),name='posts'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('post/',views.author_panel ,name= 'author_panel'),
    path('post/status/',views.author_panel_drafts ,name= 'drafts'),
    path('post/create/',views.PostCreate.as_view(), name='create'),
    path('post/<slug:slug>/edit/',views.PostUpdate.as_view(), name = 'update'),
    path('categories/',views.CategoryList.as_view(),name='categories'),
    path('category/<category>/', views.blog_category, name="blog_category"),
    path('post/done/',views.done, name = 'done'),
    path('post/edited/',views.edited, name = 'edit'),
    path('<slug:slug>/',views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/pdf/',views.PostPDFView.as_view(),name='pdf'),
]
