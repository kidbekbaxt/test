from django.db import models


class Question(models.Model):
    question = models.TextField()
    ball = models.IntegerField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.RESTRICT)
    answer = models.CharField(max_length=100)
    is_right = models.BooleanField()