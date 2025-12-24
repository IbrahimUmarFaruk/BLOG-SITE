'''from django.db import models
from django.conf import settings
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField() # We use 'body' to match your templates
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
        #return reverse('article_detail', kwargs={'pk': self.pk})
    def get_absolute_url(self):
        # UPDATE THIS LINE:
        return reverse('post_detail', kwargs={'pk': self.pk})

# models.py
from django.db import models
from django.conf import settings  # <--- You were missing this import!
from django.urls import reverse

# (Your Article model should be above this)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')'''

'''from django.db import models
from django.conf import settings
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField() # Renamed from 'body' to match standard views
    date = models.DateTimeField(auto_now_add=True) # Renamed from 'date'
    date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False) # <--- THIS IS THE MISSING FIELD
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')'''
        
from django.db import models
from django.conf import settings
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=200) 
    body = models.TextField()
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    
    date = models.DateTimeField(auto_now_add=True) 
    date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
        #return reverse('article_detail', kwargs={'pk': self.pk})
    # In models.py
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk}) # Must say 'pk', not 'slug'
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')
