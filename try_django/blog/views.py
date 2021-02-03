from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import Article
from .forms import ArticleModelForm
# Create your views here.


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()  # <blog>/<modelname>_list.html


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    #queryset = Article.objects.all()
    # queryset = Article.objects.filter(id__gt=1) #jesli id jest wieksze niz 1

    def get_object(self):
        id_ = self.kwargs.get("id")  # przekazywane addresy id
        return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return '/'


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):  # pobiera obiekt id
        id_ = self.kwargs.get("id")  # pobieranie adresu id
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):  # sprawdza wiarygodnosc kodu
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')
