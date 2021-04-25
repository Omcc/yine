from rest_framework import serializers
from question.models import Question
from question.models import Test
from question.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id','name','level']

class SubjectTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(source='get_children')
    class Meta:
        model=Subject
        fields = ('children',)
    def get_children(self,obj):
        children = self.context['children'].get(obj.id,[])
        serializer = SubjectSerializer(children,many=True,context=self.context)
        return serializer.data

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

