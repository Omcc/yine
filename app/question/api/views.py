from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from question.models import Question
from question.models import Test

from question.api.serializers import QuestionSerializer
from question.api.serializers import TestSerializer

class QuestionList(APIView):
    def get(self,request,format=None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions,many=True)
        return Response(serializer.data)
class TestList(APIView):
    def get(self,request,format=None):
        tests = Test.objects.all()
        serializer = TestSerializer(tests,many=True)
        return Response(serializer.data)
