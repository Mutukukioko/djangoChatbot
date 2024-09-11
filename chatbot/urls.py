from django.urls import path
from .views import MessageView,QuestionAnswerView,ChatbotAnswerView

urlpatterns = [
    path('message/', MessageView.as_view(), name='message'),
     path('qanswer/', QuestionAnswerView.as_view(), name='qanswer'),
     path('askme/', ChatbotAnswerView.as_view(), name='askme'),
]
