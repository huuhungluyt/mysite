from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question


def question_index(request):
	latest_questions = Question.objects.order_by('pub_time')[:5]
	#view = loader.get_template('polls/index.html')
	context = {
		'latest_questions': latest_questions,
	}
	return render(request, 'polls/index.html', context)
	#return HttpResponse(view.render(context, request));

def question_detail(request, question_id):
	try:
		question = Question.objects.get(id = question_id)
	except Question.DoesNotExist:
		raise Http404('Question not found.')
	return render(request, 'polls/question_detail.html', {'question': question})

def question_result(request, question_id):
	response = "This result page of question number %s."
	return HttpResponse(response % question_id)

def question_vote(request, question_id):
	response = "Voting for the question number %s." % question_id
	return HttpResponse(response)
