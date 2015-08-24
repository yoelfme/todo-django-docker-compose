from django.test import TestCase
from .models import Task

class TaksTest(TestCase):

    def test_create_task(self):
        """
        When create task the print object should be equals to proper text
        """
        text = 'My task'
        task = Task(text=text)
        self.assertEqual(str(task), text)
