from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    return HttpResponse('歡迎光臨本書店，來杯提神的咖啡，看本好書吧！')
