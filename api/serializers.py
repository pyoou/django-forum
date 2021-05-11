from rest_framework import serializers

from forum.models import Category, Question, Answer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'content', 'image', 'category', 'author', 'created_at', 'updated_at']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'content', 'image', 'author', 'created_at', 'updated_at']

