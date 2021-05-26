# Generated by Django 3.0.7 on 2021-05-26 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('writers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('ACCEPTED', 'ACCEPTED'), ('REJECTED', 'REJECTED'), ('PENDING', 'PENDING')], default='PENDING', max_length=40)),
                ('edited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='edited_by', to='writers.Writer')),
                ('written_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='written_by', to='writers.Writer')),
            ],
        ),
    ]
