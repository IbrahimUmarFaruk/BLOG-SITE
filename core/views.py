'''from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article
from .forms import ArticleForm
from django.shortcuts import render, get_object_or_404 
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .forms import CommentForm 
from .models import Article, Comment 

# 1. This is the function your error is looking for!
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

# 2. This is the second function for the detail page
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    success_url = reverse_lazy('article_list')
    
def search(request):
    q = request.GET.get('q','')
    articles=Article.objects.filter(title__icontains=q)
    return render(request,'article_list.html',{'articles':articles})
class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ['title', 'content'] 
    success_url = reverse_lazy('article_list')
    
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('article_list')
    login_url = 'login' 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return
        super().form_valid(form)
    
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'content']
    login_url = 'login'

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    
from django.contrib.auth.forms import UserCreationForm 

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') 
    template_name = 'registration/signup.html'
    
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    
class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'body'] '''
'''from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .models import Article
from .forms import CommentForm 
from .models import Article, Comment 
# Note: Ensure you have an forms.py if you want to use ArticleForm, 
# otherwise CreateView/UpdateView can generate forms automatically using 'fields'.
# from .forms import ArticleForm 

# --- Function Based Views ---

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})

def search(request):
    q = request.GET.get('q', '')
    articles = Article.objects.filter(title__icontains=q)
    return render(request, 'article_list.html', {'articles': articles})


# --- Class Based Views ---

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    # Make sure these field names match your models.py exactly
    fields = ['title', 'body'] 
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        # FIX: We return the result of the super() call, which returns the response
        return super().form_valid(form)'''

'''from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Article
from .forms import ArticleForm

# --- 1. HOMEPAGE & LIST VIEW ---
def article_list(request):
    # This filters for published articles, just like we set up
    articles = Article.objects.filter(published=True)
    return render(request, 'core/article_list.html', {'articles': articles})

# --- 2. DETAIL VIEW ---
def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'core/article_detail.html', {'article': article})

# --- 3. SEARCH VIEW (From your code) ---
def search(request):
    q = request.GET.get('q', '')
    # Search title, but only show published results
    articles = Article.objects.filter(title__icontains=q, published=True)
    return render(request, 'core/article_list.html', {'articles': articles})

# --- 4. SIGN UP VIEW (For Authentication) ---
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# --- 5. CREATE ARTICLE (Optional - for Editors) ---
def article_create(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save()
        # Redirect to the new article after saving
        return redirect('article_detail', slug=article.slug)
    return render(request, 'core/article_form.html', {'form': form})'''
    

'''from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# --- 1. SEARCH FUNCTION ---
def search(request):
    q = request.GET.get('q', '')
    articles = Article.objects.filter(title__icontains=q, published=True)
    return render(request, 'core/article_list.html', {'articles': articles})

# --- 2. CLASS BASED VIEWS ---

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ArticleListView(ListView):
    model = Article
    template_name = 'core/article_list.html'
    context_object_name = 'articles'
    
    def get_queryset(self):
        return Article.objects.filter(published=True)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'core/article_detail.html'
    context_object_name = 'article'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'core/article_form.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'core/article_form.html'
    login_url = 'login'

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'core/article_confirm_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'core/add_comment.html'

    def form_valid(self, form):
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)
        
    def get_success_url(self):
        article = Article.objects.get(pk=self.kwargs['pk'])
        return reverse('article_detail', kwargs={'slug': article.slug})'''
        
'''from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# --- 1. SEARCH FUNCTION (Function-Based View) ---
def search(request):
    q = request.GET.get('q', '')
    articles = Article.objects.filter(title__icontains=q, published=True)
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
    
    def get_queryset(self):
        return Article.objects.filter(published=True)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_new.html'
    login_url = 'login'

    def form_valid(self, form):
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
    
# Make sure these are imported at the top of your file
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        # 1. Automatically set the author to the logged-in user
        form.instance.author = self.request.user
        
        # 2. Automatically link the comment to the current article
        article_id = self.kwargs['pk']
        form.instance.article = get_object_or_404(Article, pk=article_id)
        
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the article page after commenting
        return reverse('article_detail', kwargs={'pk': self.kwargs['pk']})
'''
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
        return Article.objects.filter(published=True).order_by('-created_at')
    
    def get_queryset(self):
        # Only show published articles. If you don't have a 'published' field, use:
        # return Article.objects.all().order_by('-created_at')
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