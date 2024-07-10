from rest_framework import serializers

def validate_name(value):
    if not isinstance(value, str) or value.isdigit():
        raise serializers.ValidationError("Name must be a string and cannot be a number.")
    return value

def validate_bio(value):
    if not isinstance(value, str) or value.isdigit():
        raise serializers.ValidationError("Bio must be a string and cannot be a number.")
    return value
