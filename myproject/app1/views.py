from django.shortcuts import render
from django.http import HttpResponse
import math as m


def index(request):
    return render(request, 'app1/index.html')


def task1(request):
    if request.method == 'POST':
        v = float(request.POST['v'])
        a = float(request.POST['a'])
        if 'out' in request.POST:
            way = task1_way(v, a)
            time = task1_time(v, a)
            result = {
                'way': way,
                'time': time
            }
            return render(request, 'app1/task1.html', result)
    return render(request, 'app1/task1.html')


def task2(request):
    if request.method == 'POST':
        P = float(request.POST['P'])
        L = float(request.POST['L'])
        R = float(request.POST['R'])
        if 'out' in request.POST:
            N = task2_N(P, L, R)
            result = {
                'N': N
            }
            return render(request, 'app1/task2.html', result)
    return render(request, 'app1/task2.html')


def task3(request):
    if request.method == 'POST':
        P = float(request.POST['P'])
        h = float(request.POST['h'])
        D = float(request.POST['D'])
        H = float(request.POST['high'])
        p = float(request.POST['p'])
        if 'out' in request.POST:
            AB = task3_AB(h, D, H, P, p)
            result = {
                'AB': AB
            }
            return render(request, 'app1/task3.html', result)
    return render(request, 'app1/task3.html')

# Реализация решения task1


def task1_way(v, a):
    v = v/3.6
    return (v**2) / (2 * a)


def task1_time(v, a):
    v = v/3.6
    return v/a


# Реализация решения task2

def task2_N(P, L, R):
    return P/(2*m.sqrt(1-(L**2/(4*R**2))))


# Реализация решения task3

def task3_AB(h, R, H, P, p):
    b = h/2 + H
    S = R*h
    return (2 * p * S * b)/P
