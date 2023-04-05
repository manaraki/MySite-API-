from django.urls import path

from . import views

urlpatterns=[
    path('questions/',views.QuestionListView.as_view(),name='questions-list'),
    path('question/create/',views.QuestionCreateView.as_view(),name='question-create'),
    path('question/update/<int:pk>/',views.QuestionUpdateView.as_view(),name='question-update'),
    path('question/delete/<int:pk>/',views.QuestionDeleteView.as_view(),name='question-delete'),
]