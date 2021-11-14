from django.db import models

class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return f'{self.id}, {self.name}, {self.price}, {self.image}, {self.release_date}, {self.lte_exists}, {self.slug}'