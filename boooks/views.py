from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def book_list(request: HttpRequest):
    return render(request, 'base.html')
