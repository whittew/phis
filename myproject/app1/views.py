from django.shortcuts import render
from django.http import HttpResponse
import math as m


def index(request):
    return render(request, 'app1/index.html')


def task1(request):
    if request.method == 'POST':
        v = str(request.POST['v'])
        a = str(request.POST['a'])
        if v == '' or a == '':
            return render(request, 'app1/task1.html')
        v = float(v)
        a = float(a)
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
        P = str(request.POST['P'])
        L = str(request.POST['L'])
        R = str(request.POST['R'])
        if P == '' or L == '' or R == '':
            return render(request, 'app1/task2.html')
        P = float(P)
        L = float(L)
        R = float(R)
        if 'out' in request.POST:
            N = task2_N(P, L, R)
            result = {
                'N': N
            }
            return render(request, 'app1/task2.html', result)
    return render(request, 'app1/task2.html')


def task3(request):
    if request.method == 'POST':
        P = str(request.POST['P'])
        h = str(request.POST['h'])
        D = str(request.POST['D'])
        H = str(request.POST['high'])
        p = str(request.POST['p'])
        if P == '' or h == '' or D == ' ' or H == '' or p == '':
            return render(request, 'app1/task3.html')
        P = float(P)
        h = float(h)
        D = float(D)
        H = float(H)
        p = float(p)
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
