from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django_seed import Seed
import random
from passwordgenerator import pwgenerator
from faker import Faker
import datetime


class Command(BaseCommand):
    help = 'Populate 5 users in DB'

    def handle(self, *args, **kwargs):

        x = 0
        while x < 5:
            seeder = Seed.seeder()
            seeder.add_entity(User, 1, {
                'password': lambda x: pwgenerator.generate() + str(random.randint(0, 1000000000)),
                'last_login': None,
                'is_superuser': 0,
                # 'username': lambda inserted_entities: list_username,
                'username': Faker().user_name(),
                'first_name': '',
                'last_name': '',
                'email': seeder.faker.email(),
                'is_staff': 0,
                'is_active': 0,
                'date_joined': datetime.datetime.now()
            })
            seeder.execute()
            x += 1
            seeder.entities = {}
            seeder.quantities = {}
            seeder.orders = []