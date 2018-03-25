from django.db import models

# Create your models here.

class Question(models.Model):
	content = models.CharField(max_length = 128)
	pub_time = models.DateTimeField('date published')

	def __str__(self):
		return self.content

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	content = models.CharField(max_length = 256)
	vote = models.IntegerField(default = 0)

	def __str__(self):
		return self.content
