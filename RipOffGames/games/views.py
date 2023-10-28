from django.shortcuts import render

def gamesIndex(request):
    return render(request, 'games/index.html')
