from rest_framework import serializers

def validate_title(value):
    if not isinstance(value, str) or value.isdigit():
        raise serializers.ValidationError("Title must be a string and cannot be a number.")
    return value

def validate_description(value):
    if not isinstance(value, str) or value.isdigit():
        raise serializers.ValidationError("Description must be a string and cannot be a number.")
    return value
