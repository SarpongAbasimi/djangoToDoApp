from django.db import models

# Create your models here.
""" A todo model to store subited to do list """
class ToDo(models.Model):
    description=models.TextField(max_length=100)


    def __str__(self):
        return f'To do description {self.id} - {self.description}'