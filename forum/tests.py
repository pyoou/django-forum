from django.test import TestCase
from forum import models as m
from users.models import NewUser


class TestForumCategoryModel(TestCase):

    def test_category_instance(self):
        category_1 = m.Category.objects.create(name='test_category_1')
        self.assertEqual(category_1.name, 'test_category_1')
        self.assertEqual(str(category_1), category_1.name)

    def test_category_count(self):
        for i in range(5):
            m.Category.objects.create(name=str(i))
        category_count = m.Category.objects.all().count()
        self.assertEqual(category_count, 5)


class TestForumQuestionModel(TestCase):

    def test_question_instance(self):
        category_1 = m.Category.objects.create(name='test_category_1')
        user = NewUser.objects.create_user('test@test.com', 'test', 'test', 'password')
        question_1 = m.Question.objects.create(content='test_question', category=category_1, author=user)

        self.assertEqual(question_1.content, 'test_question')
        self.assertEqual(question_1.category, category_1)
        self.assertEqual(question_1.author, user)
        self.assertEqual(question_1.image, None)
        self.assertEqual(str(question_1), str(question_1.id))

    def test_question_count(self):
        category_1 = m.Category.objects.create(name='test_category_1')
        user = NewUser.objects.create_user('test@test.com', 'test', 'test', 'password')
        for i in range(5):
            m.Question.objects.create(content=str(i), category=category_1, author=user)
        question_count = m.Question.objects.all().count()
        self.assertEqual(question_count, 5)


class TestForumAnswerModel(TestCase):

    def test_answer_instance(self):
        category_1 = m.Category.objects.create(name='test_category_1')
        user = NewUser.objects.create_user('test@test.com', 'test', 'test', 'password')
        question_1 = m.Question.objects.create(content='test_question', category=category_1, author=user)
        answer_1 = m.Answer.objects.create(question_id=question_1, content='something to test', author=user)

        self.assertEqual(answer_1.question_id, question_1)
        self.assertEqual(answer_1.content, 'something to test')
        self.assertEqual(answer_1.author, user)
        self.assertEqual(str(answer_1), str(answer_1.id))

    def test_answer_count(self):
        category_1 = m.Category.objects.create(name='test_category_1')
        user = NewUser.objects.create_user('test@test.com', 'test', 'test', 'password')
        question_1 = m.Question.objects.create(content='test_question', category=category_1, author=user)
        for i in range(5):
            m.Answer.objects.create(question_id=question_1, content=str(i), author=user)
        answer_count = m.Answer.objects.all().count()

        self.assertEqual(answer_count, 5)
