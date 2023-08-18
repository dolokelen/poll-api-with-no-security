from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    question_counts = serializers.IntegerField(read_only=True)
    class Meta:
        model = models.Category
        fields = ['id', 'title', 'question_counts']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Choice
        fields = ['id', 'label']


class QuestionSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(read_only=True)
    choices = ChoiceSerializer(many=True)
    class Meta:
        model = models.Question
        fields = ['id', 'category', 'author_id', 'text', 'choices', 'comment', 'status']

    def create(self, validated_data):
        user_id = self.context['user_id']
        choice_data = validated_data.pop('choices')
        question = models.Question.objects.create(author_id=user_id, **validated_data)
        
        for choice in choice_data:
            models.Choice.objects.create(question=question, **choice)

        return question


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = ['respondant', 'country', 'county', 'community']


class RespondantSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = models.Respondant
        fields = ['user', 'gender', 'birth_date', 'occupation', 'address']