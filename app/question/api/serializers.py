from rest_framework import serializers
from question.models import Question
from question.models import Test
from question.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name']

class QuestionSerializer(serializers.ModelSerializer):
    subject= SubjectSerializer(read_only=True)
    class Meta:
        model = Question
        fields = ['subject','title','option1','option2','option3','option4','difficulty']

class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True,read_only=True)
    class Meta:
        model = Test
        fields = ['name','questions']