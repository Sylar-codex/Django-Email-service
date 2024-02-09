from django.db import models

class EmailMessenger(models.Model) :
    subject = models.CharField(max_length=25)
    body = models.CharField(max_length=200)
    to_email = models.EmailField()

    def __str__(self) :
        return f'{self.subject}'
