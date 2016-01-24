from django.db import models

# Create your models here.
class Movie(models.Model):
	name = models.CharField(max_length = 150, null = False, blank = False)
	director = models.CharField(max_length = 150, null = False, blank = False)
	popularity = models.FloatField(null = False, blank = False)
	genre = models.CharField(max_length = 200)
	imdb_score = models.FloatField(null = False, blank = False)

	def __unicode__(self):
		return self.name



