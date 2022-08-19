from django.http import HttpResponse
import random


def index(request):
    print("index view: inside application handler")
    if random.random() > 0.5:
        1/0
    return HttpResponse("Hello, world. You're at the polls index.")
