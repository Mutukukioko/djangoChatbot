from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Conversation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Conversation {self.id}"

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)  # related_name added
    sender = models.CharField(max_length=50)  # 'user' or 'bot'
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.text[:50]}"


class QuestionAnswer(models.Model):
        question = models.CharField(max_length=255)
        question_variations = models.TextField()  # Store variations of the question as a comma-separated string
        answers = models.TextField()  # Store multiple answers as a comma-separated string

        def __str__(self):
             return f"Question: {self.question}"
        def get_question_variations(self):
        # Convert the comma-separated string of variations into a list
           return self.question_variations.split(',')

        def get_answers(self):
        # Convert the comma-separated string of answers into a list
           return self.answers.split(',')
