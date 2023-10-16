import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")

import django

django.setup()

from AppTwo.models import User
from faker import Faker

fakegen = Faker()


def populate(N):
    for u in range(N):
        fake_last = fakegen.last_name()
        fake_first = fakegen.first_name()
        fake_email = fakegen.email()
        new_user = User.objects.get_or_create(
            first_name=fake_first, last_name=fake_last, email=fake_email
        )


if __name__ == "__main__":
    populate(10)
    print("Populating successfully")
