from django.db import models


class Model(models.Model):


    created = models.DateTimeField(
        help_text='Date time on which the object was created.'
    )