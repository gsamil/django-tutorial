from django.db import models

# Create your models here.

# I want my backend to have memory of a product that I created.
# https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-types


class Product(models.Model):
    title = models.CharField(max_length=120, )
    description = models.TextField(blank=True, null=True)  # blank means not mandatory
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField()
    featured = models.BooleanField(default=True, null=True)  # when adding a new field, set one of them for old objects

    def get_absolute_url(self):
        return f"/products/{self.id}/"
