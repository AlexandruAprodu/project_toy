from django.urls import path
from articles import views as articles_views

app_name = 'articles'

urlpatterns = [
    path('create-article', articles_views.create_article, name="create_article"),
    path('<int:article_id>', articles_views.modify_article, name="modify_article"),
    path('article-approval', articles_views.article_approval, name="article_approval"),
    path('reject<int:article_id>', articles_views.reject_article, name="reject_article"),
    path('accept<int:article_id>', articles_views.accept_article, name="accept_article"),
    path('articles-edited', articles_views.articles_edited, name='articles_edited'),

    ]
