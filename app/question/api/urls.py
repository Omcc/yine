from django.urls import path
from question.api import views as api_views

urlpatterns = [
    path('questions/',api_views.QuestionList.as_view()),
    path('tests/',api_views.TestList.as_view()),
]

