from django.db import models


# Contact Model
class ContactModel(models.Model):
    name = models.CharField(max_length=20, default='')
    email = models.EmailField(default='')
    phoneNumber = models.IntegerField(default=000-000-0000)

    def __str__(self):
        return self.name
