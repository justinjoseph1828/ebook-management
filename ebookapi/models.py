from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator



# Create your models here.
GENRE_CHOICES = (
    ('Fantasy', 'Fantasy'),
    ('Literary', 'Literary'),
    ('Mystery', 'Mystery'),
    ('Non-Fiction', 'Non-Fiction'),
    ('Science Fiction', 'Science Fiction'),
    ('Thriller', 'Thriller'),
)


class ebook(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    review = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    favorite=models.BooleanField(default=False)

      # ...
    def __str__(self):
        return self.title