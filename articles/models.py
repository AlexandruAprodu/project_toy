from django.db import models
from writers.models import Writer


class Article(models.Model):

    STATUS_CHOICES = (
        ('ACCEPTED', 'ACCEPTED'),
        ('REJECTED', 'REJECTED'),
        ('PENDING', 'PENDING'),
    )
    created_at = models.DateTimeField(auto_now=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, default='PENDING', max_length=40)
    written_by = models.ForeignKey(Writer, on_delete=models.PROTECT, related_name='written_by')
    edited_by = models.ForeignKey(Writer, on_delete=models.PROTECT, related_name='edited_by', null=True)
