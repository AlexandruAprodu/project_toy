##Models

###Article
```created_at
title
content
status ( APPROVE, REJECT, PENDING )
written_by (Writer)
edited_by (Writer)
 ```

###Writer - connect to Django User auth model

```
is_editor (boolean)
name 
```

###Views and Templates


#### writer summary trio
URL (located at “/”)
- this page should show a short writer summary table.
- hint: the single Django ORM query to get this information should be elegant and clean.

```
Writer Total Articles       Written Total           Articles Written Last 30
      writer.name     count(Article.objects.all())           x
      name                         x                         x
```

```
Articles Written Last 30
from datetime import datetime, timedelta
last_month = datetime.today() - timedelta(days=30)
items_count = count(Item.objects.filter(my_date__gte=last_month).order_by(...))
```

#### Article creation Page
URL (located at "/article/create")

- Allow writers to create a new article instance into the DB
- status default pending


####Writer Article Detail Page 
URL (located at “/article/<article_id>/”)
form: 
- title
- content
- status(read only)
- if this object has been modified, status chnaged from approve, reject, or pending in pending


####Article Approval Page 
URL (located at “/article-approval”)
- this page should be viewable by editors only
- list of articles without reject or approved status
- buttons of each article, approve, reject


####Articles Edited Page
URL (located at “/articles-edited”)
- this page should be viewable by editors only
```
from django.http import Http404
https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#django.contrib.admin.views.decorators.staff_member_required

if request.user.is_editor == True:
    do someth
else:
    raise Http404()
```
- this page should show all of the articles approved/rejected by the logged in editor.


database sqlite

#Requirements for this project

Django==3.1.7


#Test Cases
- dashboard sa afiseze corect baza de date
- “/article-approval” > sa dea 404 daca userul logat is_editor == False
- “/articles-edited” ca da toate articolele userului respectiv


### sa fac seed cu cativa useri si multe articole