from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200) 
    def __str__(self):              # __unicode__ on Python 2
        return self.question_text
