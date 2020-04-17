from django.test import TestCase
from todo_list.models import TodoList


class TodoListTestCase(TestCase):
    def setUp(self):
        TodoList.objects.create(
            activity='Create tests for project.',
            priority=1,
            order=1,
        )

    def test_create_and_delete(self):
        created_todo_object = TodoList.objects.filter(id=1).first()
        TodoList.objects.filter(id=1).delete()
        deleted_todo_object = TodoList.objects.filter(id=1).first()
        self.assertNotEqual(created_todo_object, None)
        self.assertEqual(deleted_todo_object, None)

    def test_post_add(self):
        response = self.client.post('/add', {
            'activity': 'Create test for post method.',
            'priority': 2,
        })
        created_object = TodoList.objects.filter(id=2).first()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(created_object.activity, 'Create test for post method.')
        self.assertEqual(created_object.priority, 2)
        self.assertEqual(created_object.status, 0)
        self.assertEqual(created_object.order, 2)

    def test_post_edit(self):
        created_object = TodoList.objects.filter(id=1).first()
        updated_activity = 'Update tests for project.'
        response = self.client.post(f'/edit/{created_object.id}', {
            'activity': updated_activity,
            'priority': created_object.priority,
        })
        created_object = TodoList.objects.filter(id=1).first()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(created_object.activity, updated_activity)

    def test_post_filter(self):
        response = self.client.post('/filter', {
            'choice': '2',
        })
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        response1 = self.client.get('/')
        self.assertEqual(response1.status_code, 200)
        response2 = self.client.get('/add')
        self.assertEqual(response2.status_code, 200)
        response3 = self.client.get('/edit/1')
        self.assertEqual(response3.status_code, 200)
