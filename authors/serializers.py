from rest_framework import serializers
from .models import Author
from .validators import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
    
    name = serializers.CharField(
        required=True, 
        allow_blank=False, 
        validators=[validate_name],
        error_messages={
            'blank': 'This field may not be blank.',
            'null': 'This field may not be null.',
        }
    )
    birth_date = serializers.DateField(
        required=True,
        validators=[validate_birth_date], 
        error_messages={
            'invalid': 'Enter a valid date.',
            'null': 'This field may not be null.',
        }
    )
    
    bio = serializers.CharField(
        required=True, 
        allow_blank=False, 
        validators=[validate_bio],
        error_messages={
            'blank': 'This field may not be blank.',
            'null': 'This field may not be null.',
        }
    )
