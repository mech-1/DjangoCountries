from django.core.management import BaseCommand

from MainApp.models import Country, Language
from MainApp.utils import json_from_file


class Command(BaseCommand):
    help = 'Импорт данные из json файла в БД'

    def handle(self, *args, **options):
        countries = []
        languages_items = set()

        countries_items = json_from_file()
        for item in countries_items:
            countries.append(item['country'])
            languages_items.update(item['languages'])
            # second variant
            # for language in item['languages']:
            #     languages_items.add(language)

        languages = sorted(languages_items)
        self.stdout.write(f"Countries:{len(countries)}, max length: {max(len(element) for element in countries)}")
        self.stdout.write(f"Languages:{len(languages)}, max length: {max(len(element) for element in languages)}")

        # Iterate over the list and add each item to the database
        # for language in languages:
        #     # Create and save a new Item object
        #     Language.objects.create(name=language)

        # Bulk Creation for Efficiency : Create a list of Language objects
        items_to_create = [Language(name=language) for language in languages]

        # Use bulk_create to add all items at once
        Language.objects.bulk_create(items_to_create)

        for item in countries_items:
            country = Country.objects.create(name=item['country'])
            for language in item['languages']:
                lang = Language.objects.get(name=language)
                country.languages.add(lang)
            country.save()

        self.stdout.write(self.style.SUCCESS("Все данные успешно добавлены"))
