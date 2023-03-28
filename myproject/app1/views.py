from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'app1/index.html')


def task1(request):
    return render(request, 'app1/task1.html')


def task2(request):
    return render(request, 'app1/task2.html')


def task3(request):
    return render(request, 'app1/task3.html')

# Реализация решения task1


def task1_way(v, a):
    v = v/3.6
    a = a/10
    S = (v**2) / (2 * a)
    return S


def task1_time(v, a):
    v = v/3.6
    a = a/10
    time = v/a
    return time


def task1_output(request):
    if request.method == 'POST':
        v = int(request.POST['v'])
        a = (request.POST['a'])
        if 'div' in request.POST:
            way = task1_way(v, a)
            time = task1_time(v, a)
            return render(request, 'task1.html', {'Путь': way}, {'Время': time})

    return render(request, 'task1.html')
