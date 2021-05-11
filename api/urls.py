from django.urls import path

from . import views as v

urlpatterns = [
    path('category-list/', v.CategoryListAPIView.as_view(), name='category_list'),
    path('question-list/', v.QuestionListAPIView.as_view(), name='question_list'),
    path('answer-list/', v.AnswerListAPIView.as_view(), name='answer_list'),
]
