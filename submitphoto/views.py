#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

import submitphoto.api as api


def index(request):
    try:
        text = api.get_text('submitphoto/images/chinese_english.jpg')
        return HttpResponse(f"this says: {text}")
    except Exception as e:
        return HttpResponse(e)