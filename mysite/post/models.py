from django.db import models


class posts(models.Model):
    title_text = models.CharField(max_length=200)
    desc_text = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title_text
        return self.desc_text
