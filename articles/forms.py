from django import forms
from articles.models import Article


class DateInput(forms.DateInput):
    input_type = 'date'


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['created_at', 'title', 'content']
        widgets = {
            'created_at': DateInput()
        }


class ModifyArticleForm(forms.ModelForm):
    status = forms.CharField(disabled=True)

    class Meta:
        model = Article
        fields = ['title', 'content', 'status']
