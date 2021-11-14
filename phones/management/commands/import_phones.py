import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('work_with_database/phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                new_phone = Phone.objects.create(
                    id=int(line[0]), name=line[1],
                    price=int(line[3]), image=line[2],
                    release_date=line[4],
                    lte_exists=line[5],
                    slug=slugify(line[1]),
                )
