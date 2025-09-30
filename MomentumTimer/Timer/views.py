from django.shortcuts import render

def timer_page(request):
    return render(request, 'Timer/timer.html', {"test": "HELLO FROM TIMER VIEW"})

