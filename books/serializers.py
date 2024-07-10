from rest_framework import serializers
from .models import Book
from .validators import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    title = serializers.CharField(
        required=True, 
        allow_blank=False, 
        validators=[validate_title],
        error_messages={
            'blank': 'This field may not be blank.',
            'null': 'This field may not be null.',
        }
    )
    
    description = serializers.CharField(
        required=True, 
        allow_blank=False, 
        validators=[validate_description],
        error_messages={
            'blank': 'This field may not be blank.',
            'null': 'This field may not be null.',
        }
    )
    
    publish_date = serializers.DateField(
        required=True, 
        error_messages={
            'invalid': 'Enter a valid date.',
            'null': 'This field may not be null.',
        }
    )
