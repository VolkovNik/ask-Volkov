from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from app.models import *
import random

first_answer = 'First of all I would like to thank you for the invitation to participate in such a... Russia is a huge territory which in many respects need to be render habitable.'

second_answer = 'Try to write about it in chat'

third_answer = 'I do not know what to do'

questions =[
	{
	'id': idx, 
	'title': f'Title {idx}',
	'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat.', 
	'like': random.randint(0, 100),
	'answers': [first_answer, second_answer, third_answer],
	'tags': ['perl', 'TechnoPark', 'bender'],
	} for idx in range (24)
]


questions[0]['answers'].pop()
questions[0]['tags'].append("Mail.ru")
questions[1]['tags'].append("Mail.ru")

tags = ['perl', 'python', 'TechnoPark', 'MySQL', 'django', 'Mail.ru', 'Firefox', 'black-jack', 'bender']

def paginate(questions, request, per_page=5):
	paginator = Paginator(questions, per_page)
	page = request.GET.get('page', 1)
	pagginated_question = paginator.page(page)
	return pagginated_question


def new_questions(request):
	profile = Profile.objects.root()
	questions = Question.objects.new_questions()
	#tags = Tag.objects.get_best_tags()

	pagginated_question = paginate(questions, request)

	return render(request, 'new_questions.html', {
		'questions': pagginated_question,
		'tags': tags,
		'profile': profile
		})

def hot_questions(request):
	questions = Question.objects.new_questions()
	pagginated_question = paginate(questions, request)

	return render(request, 'hot_questions.html', {
		'questions': pagginated_question,
		'tags': tags,
		})

def ask(request):
	return render(request, 'ask.html', {
		'tags': tags,
		})

def login(request):
	return render(request, 'login.html', {
		'tags': tags,
		})

def signup(request):
	return render(request, 'registration.html', {
		'tags': tags,
		})

def question(request, pk):

	#question = questions[pk];
	question = Question.objects.question_by_id(pk)
	pagginated_answers = paginate(question['answers'], request, 2)

	return render(request, 'question.html', {
		'answers': pagginated_answers, 
		'question': question,
		'tags': tags,
		})

def settings(request):
	return render(request, 'settings.html', {
		'tags': tags,
		})

def get_tagged(questions, tag):
	tagged_question = []
	for question in questions:
		if tag in question['tags']:
			tagged_question.append(question)
	return tagged_question

def tag(request, pk):
	#tagged_question = get_tagged(questions, pk)
	tagged_question = Question.objects.questions_by_tag(pk)
	pagginated_question = paginate(tagged_question, request)


	return render(request, 'tag.html', {
		'questions': pagginated_question,
		'tag': pk,
		'tags': tags,
		})
