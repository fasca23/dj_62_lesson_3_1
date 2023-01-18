import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        list_phones = []
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        for phone in phones:
            list_phones.append(
                {'name': phone['name'], 
                'image': phone['image'], 
                'price': phone['price'], 
                'release_date': phone['release_date'], 
                'lte_exists': phone['lte_exists']}
                )
        
        for list_phone in list_phones:
            base_phone = Phone(
                name=list_phone['name'], 
                image=list_phone['image'],
                price=list_phone['price'],
                release_date=list_phone['release_date'],
                lte_exists=bool(list_phone['lte_exists']),
                slug=('-'.join(str(list_phone['name']).split())).lower()
                )
            base_phone.save()