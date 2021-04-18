from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=300)
    taskurl = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images", default="")
    phone_no= models.IntegerField(max_length=10, default=0)

    def __str__(self):
        return self.name
