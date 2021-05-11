from django.contrib import admin
from .models import Question, Category, Answer


class CategoryAdminConfig(admin.ModelAdmin):
    list_display = ['id', 'name', 'updated_at']
    list_filter = ['id', 'updated_at']


class QuestionAdminConfig(admin.ModelAdmin):
    list_display = ['id', 'content', 'category', 'author', 'updated_at']
    list_filter = ['category', 'created_at', 'updated_at']

    list_per_page = 100


class AnswerAdminConfig(admin.ModelAdmin):
    list_display = ['id', 'question_id', 'content', 'author', 'updated_at']
    list_filter = ['created_at', 'updated_at']


admin.site.register(Category, CategoryAdminConfig)
admin.site.register(Question, QuestionAdminConfig)
admin.site.register(Answer, AnswerAdminConfig)
