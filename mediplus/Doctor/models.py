from django.db import models
from django.utils.text import slugify
from mediplus.Clinic.models import Clinic
# Create your models here.


class Doctor(models.Model):
    name=models.CharField(max_length=120)
    SPECIALITY_CHOICES=(
        ('Lor', 'Lor'),
        ('Mede', 'Mede'),
        ('Onkoloq', 'Onkoloq'),
        ('Kardioloq', 'Kardioloq'),
    )
    speciality=models.CharField(
        max_length=12,
        choices=SPECIALITY_CHOICES,

    )
    Stage=models.IntegerField()
    clinic=models.ManyToManyField(Clinic)
    Level=models.CharField(max_length=150)
    image=models.ImageField(blank=True)

    slug = models.SlugField(unique=True, default="", editable=False, max_length=130)
    def __str__(self):
        return self.name

    def get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        counter = 1
        while Doctor.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Doctor, self).save(*args, **kwargs)