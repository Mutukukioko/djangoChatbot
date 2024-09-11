from django.urls import path
from .views import MessageView,QuestionAnswerView,ChatbotAnswerView

urlpatterns = [
    path('message/', ChatbotAnswerView.as_view(), name='message'),
     path('question-answer/', QuestionAnswerView.as_view(), name='question-answer'),
     path('askme/', MessageView.as_view(), name='askme'),
]
