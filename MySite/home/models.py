from django.db import models
from django.utils.text import slugify

from accounts.models import Student
from core.models import BaseModel


class Question(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(unique=True, max_length=200)
    slug = models.SlugField(unique=True,null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student}-{self.title[:20]}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Answer(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student}-{self.question.title[:20]}'
