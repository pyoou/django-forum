from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views as v

urlpatterns = [
    path('category-list/', v.CategoryListAPIView.as_view(), name='category_list'),
    path('question-list/', v.QuestionListAPIView.as_view(), name='question_list'),
    path('answer-list/', v.AnswerListAPIView.as_view(), name='answer_list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
