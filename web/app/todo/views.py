from django.shortcuts import render, redirect, reverse
from django.views.generic import Views
from .models import Task
from redis import Redis

redis = Redis(host='redis', port=6379)


class HomeView(View):

    def get(self, request):
        tasks = Task.objects.all()
        counter = redis.incr('counter')
        return render(request, 'my_home', {
            'tasks': tasks,
            'counter': counter
        })

    def post(self, request):
        Task.objects.create(text=request.POST['text'])

        return redirect(reverse('home'))
