from django.db import models
from django.utils.translation import gettext_lazy as _

class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    birth_date = models.DateField(default=None, null=False, blank=False)
    bio = models.TextField()
    
    class Meta:
        db_table = 'authors'
                
    def __str__(self):
        return self.email
