'''from django.urls import path 
from . import views 
from . views import (SignUpView, ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleCreateView, CommentCreateView)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('article/new/', ArticleCreateView.as_view(), name='article_new'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'), 
    path('',views.ArticleListView.as_view(), name='article_list'),
    path('search/', views.search, name='search'),
    path('articles/create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('articles/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('articles/<slug:slug>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('article/<slug:slug>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
   # path('new/', ArticleCreateView.as_view(), name='article_new'), 
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
   # path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    #path('', ArticleListView.as_view(), name='article_list'),
   # path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/comment/', CommentCreateView.as_view(), name='add_comment'),
    #path('search/', views.search, name='search'),
    #path('create/', views.article_create, name='article_create'),
]'''

'''from django.urls import path
from . import views
from .views import (SignUpView, ArticleListView, ArticleDetailView, 
                    ArticleUpdateView, ArticleDeleteView, ArticleCreateView, CommentCreateView)

urlpatterns = [
    # --- Website Pages (HTML) ---
    path('', ArticleListView.as_view(), name='article_list'),
    path('search/', views.search, name='search'),
    path('signup/', SignUpView.as_view(), name='signup'),

    # --- Article CRUD ---
    path('article/new/', ArticleCreateView.as_view(), name='article_new'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),

    # --- Comments ---
    path('article/<int:pk>/comment/', CommentCreateView.as_view(), name='add_comment'),
]'''

from django.urls import path
from . import views
from .views import (SignUpView, ArticleListView, ArticleDetailView, 
                    ArticleUpdateView, ArticleDeleteView, ArticleCreateView, CommentCreateView)
from . import api_views

urlpatterns = [
    # --- Website Pages ---
    path('', ArticleListView.as_view(), name='article_list'),
    path('search/', views.search, name='search'),
    path('signup/', SignUpView.as_view(), name='signup'),

    # --- Article CRUD ---
    path('article/new/', ArticleCreateView.as_view(), name='article_new'),
    
    # [CRITICAL FIX] Only keep the 'int:pk' line. Delete the 'slug:slug' line.
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    
    path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),

    # --- Comments ---
    path('article/<int:pk>/comment/', CommentCreateView.as_view(), name='add_comment'),
    path('api/articles/', api_views.ArticleListAPI.as_view(), name='api_article_list'),
    path('api/articles/<int:pk>/', api_views.ArticleDetailAPI.as_view(), name='api_article_detail'),
]