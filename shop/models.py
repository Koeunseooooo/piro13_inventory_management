from django.db import models

# Create your models here.


class Account(models.Model):
    Name = models.TextField(max_length=50)
    Call = models.TextField(max_length=50)
    Address = models.TextField(max_length=50)

    def __str__(self):
        return '{}. {} {} {}'.format(self.id, self.Name, self.Call, self.Address )
