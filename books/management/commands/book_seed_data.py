from django.core.management.base import BaseCommand
from faker import Faker
from books.models import Book
from authors.models import Author
from handlers.loading_animation import LoadingAnimation

class Command(BaseCommand):
    help = 'Seeds the database with fake data using Faker'

    def handle(self, *args, **kwargs):
        fake = Faker()

        num_records = 10

        animation = LoadingAnimation(num_records)

        for i in range(num_records):
            # Create an Author
            name = fake.name()
            bio = fake.text(max_nb_chars=200)
            birth_date = fake.date_of_birth(minimum_age=18, maximum_age=80)
            author = Author.objects.create(name=name, bio=bio, birth_date=birth_date)

            # Create a Book associated with the Author
            title = fake.sentence(nb_words=4, variable_nb_words=True)
            description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)
            publish_date = fake.date_this_decade()

            Book.objects.create(title=title, description=description, publish_date=publish_date, author=author)

            animation.animate(i)

        animation.finish()

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
