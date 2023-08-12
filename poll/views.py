from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from .serializers import CategorySerializer, QuestionSerializer
from . models import Category, Question


def hello(request):
    return render(request, 'poll/hello.html', {'name': 'Dolokelen'})


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def destroy(self, request, *args, **kwargs):
        if Question.published.filter(category_id=self.kwargs['pk']).count() > 0:
            return Response({'error': 'Category cannot be deleted because it is associated with one or more questions.'}, 
                            status=status.HTTP_409_CONFLICT)
        return super().destroy(request, *args, **kwargs)


class QuestionViewSet(ModelViewSet):
    queryset = Question.published.all()
    serializer_class = QuestionSerializer
