from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question


def question_index(request):

	host = request.get_host()

	latest_questions = Question.objects.order_by('pub_time')[:5]
	#view = loader.get_template('polls/index.html')
	context = {
		'latest_questions': latest_questions,
		'str': host,
	}
	return render(request, 'polls/index.html', context)
	#return HttpResponse(view.render(context, request));


def question_detail(request, question_id):
	question = get_object_or_404(Question, id = question_id)
	return render(request, 'polls/question_detail.html', {'question': question})


def question_result(request, question_id):
	question = get_object_or_404(Question, id = question_id)
	return render(request, 'polls/question_result.html', {'question': question})



class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_questions'
	
	def get_queryset(self):
		return Question.objects.order_by('pub_time')[:5]


class QuestionDetailView(generic.DetailView):
	model = Question
#	template_name = 'polls/question_detail.html'


class QuestionResultView(generic.DetailView):
	model = Question
#	template_name = 'polls/question_result.html'


def question_vote(request, question_id):
	question = get_object_or_404(Question, id = question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, "polls/question_detail.html",{
			'question': question,
			'error_message': 'Did not select any one.'
		})
	selected_choice.vote += 1
	selected_choice.save()
	return HttpResponseRedirect(reverse('polls:question_result', args=(question_id,)))
