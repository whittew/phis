from django.shortcuts import render
from django.http import HttpResponse
import math as m


def index(request):
    return render(request, 'app1/index.html')


def task1(request):
    if request.method == 'POST':
        v = float(request.POST['v'])
        a = float(request.POST['a'])
        if a < 0 or v < 0:
            out_r = 'Неверные данные'
            result = {
                'out_r': out_r
            }
            return render(request, 'app1/task1.html', result)
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
        if P < 0 or L < 0 or R < 0:
            out_r = 'Неверные данные'
            result = {
                'out_r': out_r
            }
            return render(request, 'app1/task2.html', result)
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
        p = float(request.POST['p'])
        H = float(request.POST['high'])
        if P < 0 or h < 0 or D < 0 or p < 0 or H < 0:
            out_r = 'Неверные данные'
            result = {
                'out_r': out_r
            }
            return render(request, 'app1/task3.html', result)
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
    return round((v**2) / (2 * a), 3)


def task1_time(v, a):
    v = v/3.6
    return round(v/a, 3)


# Реализация решения task2

def task2_N(P, L, R):
    return round(P/(2*m.sqrt(1-(L**2/(4*R**2)))), 3)


# Реализация решения task3

def task3_AB(h, R, H, P, p):
    b = h/2 + H
    S = R*h
    return round((2 * p * S * b)/P, 3)
