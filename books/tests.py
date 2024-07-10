from django.test import TestCase
from .models import Book
from authors.models import Author
from django.core.exceptions import ValidationError
from datetime import date

class BookModelTest(TestCase):
    
    def setUp(self):
        # Create two authors
        self.author1 = Author.objects.create(name='John Doe', bio='Sample bio 1', birth_date='2000-01-01')
        self.author2 = Author.objects.create(name='Jane Doe', bio='Sample bio 2', birth_date='1995-05-15')

        # Create books associated with authors
        self.book1 = Book.objects.create(title='Book 1', description='Description 1', publish_date='2023-01-01', author=self.author1)
        self.book2 = Book.objects.create(title='Book 2', description='Description 2', publish_date='2023-02-01', author=self.author2)
        
    def test_create_book(self):
        book = Book.objects.create(
            title='Sample Book',
            description='Sample description',
            publish_date=date(2023, 1, 1),
            author=self.author1
        )

        book.full_clean()

        # Assertions to verify the created book
        self.assertEqual(book.title, 'Sample Book')
        self.assertEqual(book.description, 'Sample description')
        self.assertEqual(book.publish_date, date(2023, 1, 1))
        self.assertEqual(book.author, self.author1) 
    
    def test_get_all_books(self):
        all_books = Book.objects.all()

        self.assertEqual(all_books.count(), 2)

        for book in all_books:
            if book.author == self.author1:
                self.assertEqual(book.title, 'Book 1')
                self.assertEqual(book.description, 'Description 1')
            elif book.author == self.author2:
                self.assertEqual(book.title, 'Book 2')
                self.assertEqual(book.description, 'Description 2')
            else:
                self.fail(f"Unexpected book with author {book.author}")
    
    def test_get_book_by_id(self):
        book = Book.objects.create(
            title='Sample Book',
            description='Sample description',
            publish_date=date(2023, 1, 1),
            author=self.author1
        )
        
        fetched_book = Book.objects.get(pk=book.pk)
        
        self.assertEqual(fetched_book.title, 'Sample Book')
        self.assertEqual(fetched_book.description, 'Sample description')
        self.assertEqual(fetched_book.publish_date, date(2023, 1, 1))
        self.assertEqual(fetched_book.author, self.author1) 
    
    def test_get_book_by_nonexistent_id(self):
        nonexistent_id = 9999 
        
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(pk=nonexistent_id)
    
    def test_update_author(self):
        book = Book.objects.create(
            title='Sample Book',
            description='Sample description',
            publish_date=date(2023, 1, 1),
            author=self.author1
        )       
        book.title = 'Sample Book 1'
        book.description = 'Sample description 1'
        book.publish_date = date(2023, 1, 1)
        book.author = self.author1
        book.save()
        
        updated_book = Book.objects.get(pk=book.pk)
        
        self.assertEqual(updated_book.title, 'Sample Book 1')
        self.assertEqual(updated_book.description, 'Sample description 1')
        self.assertEqual(updated_book.publish_date, date(2023, 1, 1))
        self.assertEqual(updated_book.author, self.author1)
    
    def test_delete_book(self):
        book = Book.objects.create(
            title='Sample Book',
            description='Sample description',
            publish_date=date(2023, 1, 1),
            author=self.author1
        )    
        
        book.delete()
        
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(pk=book.pk)
    
    def test_title_field_only_accepts_string(self):
        book = Book.objects.create(
            title=123,
            description='Sample description',
            publish_date=date(2023, 1, 1),
            author=self.author1
        )    
        book.full_clean()
                    
    def test_description_field_only_accepts_string(self):
        book = Book.objects.create(
            title="Jhon",
            description=123,
            publish_date=date(2023, 1, 1),
            author=self.author1
        )    
        book.full_clean()
    
    def test_empty_title_raises_validation_error(self):
        with self.assertRaises(ValidationError) as context:
            book = Book.objects.create(
                title="",
                description=123,
                publish_date=date(2023, 1, 1),
                author=self.author1
            )    
            book.full_clean()
        
        self.assertIn('title', context.exception.message_dict)
        self.assertIn('This field cannot be blank.', context.exception.message_dict['title'])
    
    def test_empty_description_raises_validation_error(self):
        with self.assertRaises(ValidationError) as context:
            book = Book.objects.create(
                title="Jhon",
                description="",
                publish_date=date(2023, 1, 1),
                author=self.author1
            )    
            book.full_clean()
        
        self.assertIn('description', context.exception.message_dict)
        self.assertIn('This field cannot be blank.', context.exception.message_dict['description'])