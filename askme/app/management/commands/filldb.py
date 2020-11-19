from django.core.management.base import BaseCommand
from app.models import *
from faker import Faker
from random import choice
from django.contrib.auth.models import User

f = Faker()


class Command(BaseCommand):
	help = 'fill database'

	def add_arguments(self, parser):
		parser.add_argument('--questions', type=int)
		parser.add_argument('--answers', type=int)
		parser.add_argument('--tags', type=int)
		parser.add_argument('--users', type=int)

	def handle(self, *argc, **options):
		size = options['questions']
		profiles_size = options['users']
		tags_size = options['tags']
		if (options['users']):
			self.fill_profiles(profiles_size)
		if (options['tags']):
			self.fill_tags(tags_size)
		if (options['questions']):
			self.fill_questions(size)
		if (options['answers']):
			self.fill_answers(options['answers'])
		

	def fill_tags(self, cnt):
		for i in range(cnt):
			Tag.objects.create(
					title=f.sentence()[:128],
				)


	def fill_questions(self, cnt):
		tags_ids = list(
			Tag.objects.values_list(
				'id', flat=True
			)
		)
		profile_ids = list(
			Profile.objects.values_list(
				'id', flat=True
			)
		)
		for i in range(cnt):
			question = Question.objects.create(
					profile_id=choice(profile_ids),
					text=''.join(f.sentences(f.random_int(min=2, max=5))),
					title=f.sentence()[:128],
					
				)
			question.tag.add(choice(tags_ids))

	def fill_answers(self, cnt):
		questions_ids = list(
				Question.objects.values_list(
						'id', flat=True
					)
			)
		profile_ids = list(
			Profile.objects.values_list(
				'id', flat=True
			)
		)
		for i in range(cnt):
			Answer.objects.create(
					text=''.join(f.sentences(f.random_int(min=2, max=5))),
					title=f.sentence()[:128],
					profile_id=choice(profile_ids),
					question_id=choice(questions_ids),
					correct_flag=choice([True, False])
				)

	def fill_profiles(self, cnt):
		users_ids = list(
			User.objects.values_list(
				'id', flat=True
			)
		)
		for i in range(cnt):
			Profile.objects.create(
					user_id=choice(users_ids),
					nickname=f.name(),
				)
