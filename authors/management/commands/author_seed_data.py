# In your_app/management/commands/seed_data.py

from django.core.management.base import BaseCommand
from faker import Faker
from authors.models import Author  # Import your model(s) here
from handlers.loading_animation import LoadingAnimation

class Command(BaseCommand):
    help = 'Seeds the database with fake data using Faker'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Number of records to create
        num_records = 1000

        # Initialize loading animation
        animation = LoadingAnimation(num_records)

        # Generate and save fake data
        for i in range(num_records):
            name = fake.name()
            bio = fake.text(max_nb_chars=200)
            birth_date = fake.date_of_birth(minimum_age=18, maximum_age=80)

            # Create an Author object with generated data
            Author.objects.create(name=name, bio=bio, birth_date=birth_date)

            # Update loading animation
            animation.animate(i)

        # Finish loading animation
        animation.finish()

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
