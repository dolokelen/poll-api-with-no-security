from django.shortcuts import render

def hello(request):
    return render(request, 'poll/hello.html', {'name': 'Dolokelen'})