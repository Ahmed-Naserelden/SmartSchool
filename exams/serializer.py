from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Exam, Question, ExamAttempt, StudentAnswer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['pk', 'answer']

class ExamSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    # questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = '__all__'
        
    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        exam = Exam.objects.create(**validated_data)
        for question_data in  questions_data:
            q = Question.objects.create(**question_data)
            exam.questions.add(q)
        # validated_data['questions_data'] = questions_data
        return exam

class StudentAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentAnswer
        fields = '__all__'

class ExamAttemptSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExamAttempt
        fields = '__all__'

class StudentExamAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswer
        fields = ['pk', 'question', 'answer']