from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from collections import defaultdict

from question.models import Question
from question.models import Test,Subject

from rest_framework import viewsets

from question.api.serializers import QuestionSerializer,SubjectSerializer,TestSerializer,SubjectTreeSerializer


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

class SubjectList(APIView):
    def get(self,request,format=None):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects,many=True)
        return Response(serializer.data)

class SubjectTreeViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectTreeSerializer

    @action(detail=True)
    def tree(self, request, pk=None):
        """
        Detail route of an category that returns it's descendants in a tree structure.
        """
        subject = self.get_object()
        descendants = subject.get_descendants()  # add here any select_related/prefetch_related fields to improve api performance

        children_dict = defaultdict(list)
        for descendant in descendants:
            children_dict[descendant.get_parent().pk].append(descendant)

        context = self.get_serializer_context()
        context['children'] = children_dict
        serializer = SubjectTreeSerializer(subject, context=context)
        return Response(serializer.data)