from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ProfileManager(models.Manager):
	def root(self):
		return self.first()

class Profile(models.Model):
	nickname = models.CharField(max_length=256, verbose_name='Никнейм')
	avatar= models.ImageField(upload_to='uploads/', verbose_name='Avatar')
	user = models.OneToOneField(User, verbose_name='Юзер', on_delete=models.CASCADE)

	objects = ProfileManager()

	def __str__(self):
		return self.nickname

	class Meta:
		verbose_name = 'Профиль'
		verbose_name_plural = 'Профили'

class Answer(models.Model):
	title = models.CharField(max_length=1024, verbose_name='Заголовок')
	text = models.TextField(verbose_name='Текст')
	correct_flag = models.BooleanField(verbose_name='Верный ответ')
	question = models.ForeignKey('Question', on_delete=models.CASCADE)
	#like
	profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

	def __str__(self):
		return self.title
		
	class Meta:
		verbose_name = 'Ответ'
		verbose_name_plural = 'Ответы'

class TagManager(models.Model):
	def get_best_tags(self):
		return self.all()[:10]

class Tag(models.Model):
	title = models.CharField(max_length=1024, verbose_name='Тэг')
	#question = models.ManyToManyField('Question')

	objects = TagManager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Тэг'
		verbose_name_plural = 'Тэги'

class Like(models.Model):
	profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
	question = models.ForeignKey('Question', on_delete=models.CASCADE)
	answer = models.ForeignKey('Answer', on_delete=models.CASCADE)
	like_flag = models.BooleanField(verbose_name='Лайк?')

	def __str__(self):
		return self.like_flag

	class Meta:
		verbose_name = 'Лайк'
		verbose_name_plural = 'Лайки'
		
class QuestionManager(models.Manager):
	def new_questions(self):
		return self.all().order_by('-date_of_create')
	def questions_by_tag(self, tag):
		return self.filter(tag__title = tag)
	def question_by_id(self, question_id):
		return self.get(pk=question_id)

class Question(models.Model):
	title = models.CharField(max_length=1024, verbose_name='Заголовок')
	text = models.TextField(verbose_name='Текст вопроса')
	profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
	date_of_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
	tag = models.ManyToManyField('Tag')

	objects = QuestionManager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Вопрос'
		verbose_name_plural = 'Вопросы'

##
##
###
####
######
