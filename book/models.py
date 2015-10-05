from django.db import models
from django.template.defaultfilters import slugify
import datetime
# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=400, blank=False, null=False)
    slug = models.CharField(max_length=150, unique=True)
    note = models.TextField()
    page_no = models.IntegerField(default=0)
    pdf = models.FileField(upload_to='%d/%m/%Y')
    date = models.DateField(auto_now_add=True, auto_now=True)

    def save(self):
        super().save()
        date = datetime.date.today()
        self.slug = '%i/%i/%i/%s' % (
            date.year, date.month, date.day, slugify(self.name)
        )
        super().save()
