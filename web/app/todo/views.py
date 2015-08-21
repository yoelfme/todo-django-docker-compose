from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from .models import Task
# from redis import Redis

# redis = Redis(host='redis', port=6379)


class HomeView(View):

    def get(self, request):
        tasks = Task.objects.all()
        # counter = redis.incr('counter')
        counter = 0
        return render(request, 'todo/_base.html', {
            'tasks': tasks,
            'counter': counter
        })

    def post(self, request):
        Task.objects.create(text=request.POST['text'])

        return redirect(reverse('home'))
