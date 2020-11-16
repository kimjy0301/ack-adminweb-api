from django.db import models


class CoreModel(models.Model):

    created = models.DateTimeField(auto_now_add=True, db_column="CREATED")
    updated = models.DateTimeField(auto_now=True, db_column="UPDATED")

    class Meta:
        abstract = True
