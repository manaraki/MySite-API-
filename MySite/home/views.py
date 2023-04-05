from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from home.models import Question
from home.serializers import QuestionSerializer


class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        ser_data = QuestionSerializer(instance=questions, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
    def post(self, request):
        ser_data = QuestionSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        ser_data = QuestionSerializer(instance=question, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({'message': 'question deleted'}, status=status.HTTP_200_OK)
