from rest_framework import serializers
from .models import Conversation, Message, QuestionAnswer

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'conversation', 'sender', 'text', 'timestamp']

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)  # Nested message data

    class Meta:
        model = Conversation
        fields = ['id', 'created_at', 'messages']

class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
         model= QuestionAnswer
         fields = ['id', 'question', 'question_variations', 'answers']
