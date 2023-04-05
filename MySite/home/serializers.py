from rest_framework import serializers

from home.models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    student = serializers.StringRelatedField(read_only=True)  # show user in order of str method (default:id)

    class Meta:
        model = Question
        fields = '__all__'

    # connect field to method
    def get_answers(self, obj):
        # via related name
        result = obj.answers.all()
        return AnswerSerializer(instance=result, many=True).data


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
