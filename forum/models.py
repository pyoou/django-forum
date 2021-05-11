from django.db import models
from users.models import NewUser


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    content = models.TextField(max_length=700)
    image = models.ImageField(verbose_name='question image', upload_to='question-images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, to_field='id', null=True)
    author = models.ForeignKey(NewUser, on_delete=models.RESTRICT, to_field='id')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.RESTRICT, to_field='id')
    content = models.TextField(verbose_name='answer content', max_length=800)
    image = models.ImageField(verbose_name='answer image', upload_to='answer-images/', blank=True, null=True)
    author = models.ForeignKey(NewUser, on_delete=models.RESTRICT, to_field='id')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
