from django.db import models
from django.utils.translation import gettext_lazy as _
from authors.models import Author

class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    publish_date = models.DateField(default=None, null=False, blank=False)
    
    class Meta:
        db_table = 'books'
                
    def __str__(self):
        return self.title
