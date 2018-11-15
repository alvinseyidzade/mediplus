from django.db import models
from django.utils.text import slugify


# Create your models here.

class Clinic(models.Model):
    slug = models.SlugField(unique=True, default="", editable=False, max_length=130)
    number=models.CharField(max_length=120)
    name=models.CharField(max_length=120)
    location=models.CharField(max_length=120)
    image=models.ImageField(blank=True)

    def __str__(self):
        return self.name
    def get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        counter = 1
        while Clinic.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Clinic, self).save(*args, **kwargs)


