from django.shortcuts import render, get_object_or_404
from articles.forms import ArticleForm, ModifyArticleForm
from articles.models import Article
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import Http404


@login_required
def create_article(request):
    if request.method == "POST":
        postForm = ArticleForm(request.POST)
        if postForm.is_valid():
            post_form = postForm.save(commit=False)
            post_form.written_by = request.user.writer
            post_form.status = 'PENDING'
            post_form.save()
            return HttpResponseRedirect(reverse('writers:dashboard'))
        else:
            print(postForm.errors)
    else:
        postForm = ArticleForm()
        return render(request, 'articles/create_article.html', {'postForm': postForm})



@login_required
def modify_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    postForm = ModifyArticleForm(request.POST or None, instance=article)
    if request.method == "POST":
        if postForm.is_valid():
            post_form = postForm.save(commit=False)
            post_form.created_at = article.created_at
            post_form.edited_by = request.user.writer
            post_form.status = 'PENDING'
            post_form.save()
            return HttpResponseRedirect(reverse('articles:article_approval'))
        else:
            print(postForm.errors)
    return render(request, 'articles/modify_article.html', {'postForm': postForm})


@login_required
def article_approval(request):
    if request.user.writer.is_editor:
        pending_articles = Article.objects.filter(status='PENDING')
        return render(request, 'articles/article_approval.html', {'pending_articles': pending_articles})
    raise Http404()


def reject_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.status = 'REJECTED'
    article.edited_by = request.user.writer
    article.save()
    return render(request, 'articles/confirmation_status_article.html')


def accept_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.status = 'ACCEPTED'
    article.edited_by = request.user.writer
    article.save()
    return render(request, 'articles/confirmation_status_article.html')


def articles_edited(request):
    if request.user.writer.is_editor:
        edited_articles = Article.objects.filter(edited_by=request.user.writer.id)
        return render(request, 'articles/articles_edited.html', {'edited_articles': edited_articles})
    raise Http404()
