from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'title']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Choice
        fields = ['id', 'label']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    class Meta:
        model = models.Question
        fields = ['id', 'category', 'author', 'text', 'choices', 'comment', 'status']

    def create(self, validated_data):
        choice_data = validated_data.pop('choices')
        question = models.Question.objects.create(**validated_data)
        
        for choice in choice_data:
            models.Choice.objects.create(question=question, **choice)

        return question

  