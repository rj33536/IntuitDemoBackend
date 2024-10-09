from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.functions import Upper

def validate_min_length(value):
    if len(value) < 7:
        raise ValidationError(f"Username must be at least 7 characters long")


class User(models.Model):
    username = models.CharField(max_length=100, unique=True, validators=[
       validate_min_length  # Add a validator
    ])
    events = models.TextField(default="[]")
    class Meta:
        constraints = [
            models.UniqueConstraint(Upper('username'), name='unique_upper_username')
        ]