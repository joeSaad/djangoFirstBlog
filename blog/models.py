from django.db import models

# Create your models here.
class posts(models.Model):
	authorID = models.IntegerField()
	title = models.CharField(max_length = 100)
	timestamp = models.DateTimeField(auto_now_add = True)
	bodyText = models.TextField()


class authors(models.Model):
	authorName = models.CharField(max_length = 40)
	authorID = models.AutoField(primary_key = True)

