
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# --- 1. SEARCH FUNCTION ---
def search(request):
    q = request.GET.get('q', '')
    # Check if 'published' exists in your model. If not, remove 'published=True'
    articles = Article.objects.filter(title__icontains=q) 
    return render(request, 'article_list.html', {'articles': articles})

# --- 2. CLASS BASED VIEWS ---

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 5  
    
    def get_queryset(self):
        return Article.objects.filter(published=True).order_by('-date')
    

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

# --- CLEANED UP CREATE VIEW ---
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    # I changed this to 'article_form.html' so it matches your UpdateView
    template_name = 'article_form.html' 
    login_url = 'login'

    def form_valid(self, form):
        # Automatically set the author to the logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    login_url = 'login'

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

# --- COMMENT VIEW ---
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        article_id = self.kwargs['pk']
        form.instance.article = get_object_or_404(Article, pk=article_id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.kwargs['pk']})