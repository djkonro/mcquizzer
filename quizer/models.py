from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=64) #(unique=True)
	def __str__(self):
		return self.title

class Question(models.Model):
	quiz = models.ForeignKey(Quiz)
	question_text = models.CharField(max_length=200)
	answer = models.IntegerField(default=0)
	def __str__(self):
		return self.question_text
		
class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	def __str__(self):
		return self.choice_text
		
class Score(models.Model):
	score = models.IntegerField(default=0)
	user = models.ForeignKey(User)
	quiz = models.ForeignKey(Quiz)
	def __str__(self):
		return self.quiz.title

