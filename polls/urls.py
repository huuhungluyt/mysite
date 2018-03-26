from django.urls import path

from . import views

app_name = 'polls'
urlpatterns=[
	path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name = 'question_detail'),
	path('questions/<int:pk>/result/', views.QuestionResultView.as_view(), name='question_result'),
	path('questions/<int:question_id>/vote/', views.question_vote, name='question_vote'),
#	path('questions/', views.IndexView.as_view(), name="question_index"),


	path('questions/', views.question_index, name="question_index"),
#	path('questions/<int:question_id>', views.question_detail, name='question_detail'),
#	path('questions/<int:question_id>/result', views.question_result, name='question_result'),
]
