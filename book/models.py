from django.db import models
from django.template.defaultfilters import slugify
import datetime
# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=400, blank=False, null=False)
    slug = models.CharField(max_length=150, unique=True)
    note = models.TextField()
    finished = models.BooleanField(default=False)
    page_no = models.IntegerField(default=0)
    pdf = models.FileField(upload_to='hiren/%Y/%m/%d')
    added_at = models.DateField(auto_now_add=True)
    finished_at = models.DateField(null=True, blank=True)

    def save(self):
        super().save()
        date = datetime.date.today()
        self.slug = '%i/%i/%i/%s' % (
            date.year, date.month, date.day, slugify(self.name)
        )
        super().save()
