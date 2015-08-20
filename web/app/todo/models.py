from django.db import models


class Task(models.Model):
    """
    This class represent a task of our TODO
    """
    text = models.TextField(blank=False, null=False)
    pub_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.text
