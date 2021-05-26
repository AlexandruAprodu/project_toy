from django.db.models import Count, Q
from django.shortcuts import render
from articles.models import Article
from .forms import RegistrationForm
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import datetime


@csrf_exempt
def register(request):
    if request.method == 'POST':
        user = RegistrationForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect(reverse('writers:login'))
    else:
        user = RegistrationForm()
    return render(request, 'writers/register.html', {'user': user, 'title': 'Register'})


def dashboard(request):
    date_minus_30 = datetime.datetime.today() - datetime.timedelta(days=30)
    writers = Article.objects.select_related('written_by') \
        .values('written_by__name__username', 'written_by__name__email') \
        .annotate(
            Count('id'),
            count_last_30=Count('id', filter=Q(created_at__gte=date_minus_30))
        )\
        .all()

    context = {
        'writers': writers
    }

    return render(request, 'writers/dashboard.html', context)
