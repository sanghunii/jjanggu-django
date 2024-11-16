from .models import Question
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
##QuestionSerializer는 serializers.ModelSerializer를 상속한다.
##model = Quesiton  =>  Question model을 serialization하는데 사용됨.
##fields = '__all__'  =>  Question model의 전체 field를 모두 serialization한다.


"""
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ("question_text",)
##QuestionSerializer는 serializers.ModelSerializer를 상속한다.
##model = Quesiton  =>  Question model을 serialization하는데 사용됨.
##fields = '__all__'  =>  Question model의 전체 field를 모두 serialization한다.

"""