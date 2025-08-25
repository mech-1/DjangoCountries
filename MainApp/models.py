from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)
    languages = models.ManyToManyField(to='Language')

    def __str__(self):
        return self.name
        # return f"Country: {self.name}"


class Language(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
        # return f"Language: {self.name}"
