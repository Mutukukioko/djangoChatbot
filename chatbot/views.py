from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Conversation, Message,QuestionAnswer
from .serializers import ConversationSerializer, QuestionAnswerSerializer
import random  # For simple bot responses
import spacy
import random
nlp = spacy.load('en_core_web_sm')

class MessageView(APIView):
    def post(self, request):
        text = request.data.get('text')

        # Create a new conversation or use the most recent one (optional)
        conversation = Conversation.objects.create()

        # Save user message
        user_message = Message.objects.create(conversation=conversation, sender='user', text=text)

        # Process message with NLP (simple logic for now)
        doc = nlp(text)
        intents = [ent.text for ent in doc.ents]

        # Generate bot response based on NLP
        if intents:
            bot_text = f"I see you're talking about {', '.join(intents)}."
        else:
            bot_text = "Sorry, I didn't understand that."

        # Save bot message
        bot_message = Message.objects.create(conversation=conversation, sender='bot', text=bot_text)

        # Return the conversation with messages
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuestionAnswerView(APIView):
    def post(self, request):
        serializer = QuestionAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        questions = QuestionAnswer.objects.all()
        serializer =QuestionAnswerSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChatbotAnswerView(APIView):
    
    def post(self, request):
        user_question = request.data.get('text', '').lower()

        # Find the matching question or variation
        question_answer = None
        all_questions = QuestionAnswer.objects.all()
        for qa in all_questions:
            variations = qa.get_question_variations()
            if user_question in [q.lower() for q in [qa.question] + variations]:
                question_answer = qa
                break
        
        if question_answer:
            # Pick a random answer
            answers = question_answer.get_answers()
            answer = random.choice(answers)
            return Response({"answer": answer}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "I don't know the answer to that."}, status=status.HTTP_404_NOT_FOUND)
