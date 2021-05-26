from articles.models import Article
from writers.models import Writer
from django.core.management.base import BaseCommand
from django_seed import Seed
import random

from faker import Faker
import datetime


class Command(BaseCommand):
    help = 'Populate 300 articles in DB'

    def handle(self, *args, **kwargs):
        all_writers = Writer.objects.all()
        statuses = ['ACCEPTED', 'REJECTED', 'PENDING']
        x = 0
        while x < 30:

            # getting a random date between a given range
            start_date = datetime.date(2021, 4, 1)
            end_date = datetime.date(2021, 5, 26)
            time_between_dates = end_date - start_date
            days_between_dates = time_between_dates.days
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)

            seeder = Seed.seeder()
            seeder.add_entity(Article, 1, {
                'created_at': random_date,
                'title': Faker().sentence(),
                'content': Faker().text(),
                'status': 'PENDING',
                'written_by': random.choice(all_writers),
                'edited_by': None,

            })
            seeder.execute()
            x += 1
            seeder.entities = {}
            seeder.quantities = {}
            seeder.orders = []