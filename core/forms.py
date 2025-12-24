from django import forms
from .models import Article
from .models import Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'body']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if 'spam' in title.lower():
            raise forms.ValidationError('Title contains disallowed word')
        return title

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment'] 
        widgets = {'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),}

'''class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body']
    def clean_title(self):
        form_class = self.cleaned_data['title']
        if 'spam' in title.lower():
            raise
        forms.ValidationError('Title contain disallowed word')
        return title

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        field = ('comment',) 
        widgets = {'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),}'''

