from django.db import models
from django.template.defaultfilters import slugify
import datetime
# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=400)
    slug = models.CharField(max_length=150, unique=True)
    note = models.TextField()
    finished = models.BooleanField(default=False)
    page_no = models.IntegerField(default=0)
    pdf = models.FileField(upload_to='hiren/%Y/%m/%d', null=True, blank=True)
    url = models.URLField(max_length=2000, null=True, blank=True)
    current_url = models.URLField(max_length=2000, null=True, blank=True)
    added_at = models.DateField(auto_now_add=True)
    finished_at = models.DateField(null=True, blank=True)

    def save(self, **kwargs):
        super().save()
        date = datetime.date.today()
        self.slug = '%i/%i/%i/%s' % (
            date.year, date.month, date.day, slugify(self.name)
        )
        super().save()
