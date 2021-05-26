from writers.models import Writer
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django_seed import Seed
import random


class Command(BaseCommand):
    help = 'Populate 7 writers in DB'

    def handle(self, *args, **kwargs):
        all_users = User.objects.all()
        name_id = 0
        x = 0
        while x < 7:
            seeder = Seed.seeder()
            seeder.add_entity(Writer, 1, {
                'name': all_users[name_id],
                'is_editor': random.choice([True, False]),

            })
            seeder.execute()
            name_id += 1
            x += 1
            seeder.entities = {}
            seeder.quantities = {}
            seeder.orders = []
