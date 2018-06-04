'''
chat view
'''
from django.shortcuts import render

# Create your views here.


def index(request):
    '''
    index view
    '''
    return render(request, 'chat/index.html', {})
