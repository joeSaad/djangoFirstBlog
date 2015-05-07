from django.db import models

# Create your models here.
class posts(models.Model):
	author = models.CharField(max_length = 40)
	title = models.CharField(max_length = 100)
	timestamp = models.DateTimeField()
	bodyText = models.TextField()

