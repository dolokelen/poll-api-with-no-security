from collections import Counter
from django.shortcuts import render
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from .serializers import CategorySerializer, QuestionSerializer, RespondantSerializer, ResponseSerializer, SelectionChoiceSerializer
from . models import Category, Question, Respondant, Response as PollResponse, SelectedChoice


def hello(request):
    return render(request, 'poll/hello.html', {'name': 'Dolokelen'})


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(question_counts=Count('questions'))
    serializer_class = CategorySerializer

    def destroy(self, request, *args, **kwargs):
        if Question.published.filter(category_id=self.kwargs['pk']).count() > 0:
            return Response({'error': 'Category cannot be deleted because it is associated with one or more questions.'}, 
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)


class QuestionViewSet(ModelViewSet):
    queryset = Question.published.prefetch_related('choices').order_by('-date_created')
    serializer_class = QuestionSerializer

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}


class RespondantViewSet(ModelViewSet):
    queryset = Respondant.objects.select_related('address', 'user').all()
    serializer_class = RespondantSerializer


class PollResponseViewSet(ModelViewSet):
    queryset = PollResponse.objects.prefetch_related('respondant', 'question').all()
    serializer_class = ResponseSerializer


class SelectedChoiceViewSet(ModelViewSet):
    queryset = SelectedChoice.objects.all()
    serializer_class = SelectionChoiceSerializer