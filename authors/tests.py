from django.test import TestCase
from .models import Author
from django.core.exceptions import ValidationError

class AuthorModelTest(TestCase):
    
    def test_create_author(self):
        author = Author(name='John Doe', birth_date='2000-01-01', bio='Sample bio')
        author.full_clean() 
    
    def test_get_all_authors(self):
        author1 = Author.objects.create(name='John Doe', birth_date='2000-01-01', bio='Sample bio 1')
        author2 = Author.objects.create(name='Jane Doe', birth_date='1995-05-15', bio='Sample bio 2')

        all_authors = Author.objects.all()

        self.assertEqual(all_authors.count(), 2)

        for author in all_authors:
            if author.pk == author1.pk:
                self.assertEqual(author.name, 'John Doe')
                self.assertEqual(author.bio, 'Sample bio 1')
            elif author.pk == author2.pk:
                self.assertEqual(author.name, 'Jane Doe')
                self.assertEqual(author.bio, 'Sample bio 2')
            else:
                self.fail(f"Unexpected author with PK {author.pk}")
    
    def test_get_author_by_id(self):
        author = Author.objects.create(name='John Doe', birth_date='2000-01-01', bio='Sample bio')

        fetched_author = Author.objects.get(pk=author.pk)
        
        self.assertEqual(fetched_author.name, 'John Doe')
        self.assertEqual(fetched_author.bio, 'Sample bio')
    
    def test_get_author_by_nonexistent_id(self):
        nonexistent_id = 9999 
        
        with self.assertRaises(Author.DoesNotExist):
            Author.objects.get(pk=nonexistent_id)
    
    def test_update_author(self):
        author = Author.objects.create(name='Jane Doe', birth_date='1990-05-15', bio='Another bio')        
        author.name = 'Jane Smith'
        author.bio = 'Updated bio'
        author.save()
        
        updated_author = Author.objects.get(pk=author.pk)
        
        self.assertEqual(updated_author.name, 'Jane Smith')
        self.assertEqual(updated_author.bio, 'Updated bio')
    
    def test_delete_author(self):
        author = Author.objects.create(name='John Doe', birth_date='2000-01-01', bio='Sample bio')
        
        author.delete()
        
        with self.assertRaises(Author.DoesNotExist):
            Author.objects.get(pk=author.pk)
    
    def test_name_field_only_accepts_string(self):
        author = Author(name=123, birth_date='2000-01-01', bio='Sample bio')
        author.full_clean()
                    
    def test_bio_field_only_accepts_string(self):
        author = Author(name='John Doe', birth_date='2000-01-01', bio=123)
        author.full_clean()
    
    def test_empty_name_raises_validation_error(self):
        with self.assertRaises(ValidationError) as context:
            author = Author.objects.create(name='', birth_date='2000-01-01', bio='Sample bio')
            author.full_clean() 
        
        self.assertIn('name', context.exception.message_dict)
        self.assertIn('This field cannot be blank.', context.exception.message_dict['name'])
    
    def test_empty_bio_raises_validation_error(self):
        with self.assertRaises(ValidationError) as context:
            author = Author.objects.create(name='Jhon', birth_date='2000-01-01', bio='')
            author.full_clean() 
        
        self.assertIn('bio', context.exception.message_dict)
        self.assertIn('This field cannot be blank.', context.exception.message_dict['bio'])