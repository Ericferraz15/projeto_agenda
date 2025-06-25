import django
import os
import sys
from pathlib import Path
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ["DJANGO_SETTINGS_MODULE"] = "project.settings"
settings.USE_TZ = False

django.setup()

if __name__ == "__main__":
    import faker
    from random import choice
    from contact.models import Contact, category

    Contact.objects.all().delete()
    category.objects.all().delete()

    fake = faker.Faker('pt_BR')
    categories = ["amigos", "familia", "trabalho",]

    django_categories = [category(name=name) for name in categories]

    for django_category in django_categories:
        django_category.save()

    django_contacts = []
    for _ in range(NUMBER_OBJECTS):
        profile = fake.simple_profile()
        email = profile['mail']
        first_name, last_name = profile['name'].split(" ", 1)  # type: ignore
        phone = fake.phone_number()
        created_date = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)
        

        django_contacts.append(
        Contact(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            created_date=created_date,
            description=description,
            Category= category,
        )
        )

if len(django_contacts) > 0:
    Contact.objects.bulk_create(django_contacts)
