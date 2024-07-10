from rest_framework import serializers

def validate_name(value):
    if not isinstance(value, str) or value.isdigit():
        raise serializers.ValidationError("Name must be a string and cannot be a number.")
    return value

def validate_birth_date(value):
    if not isinstance(value, str):
        raise serializers.ValidationError("Birth date must be valid format and cannot be a string.")
    return value

def validate_bio(value):
    if not isinstance(value, str) or value.isdigit():
        raise serializers.ValidationError("Bio must be a string and cannot be a number.")
    return value
