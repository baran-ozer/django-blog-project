from django.http.response import HttpResponse
from django.shortcuts import render

def main(request):
    return render(request, 'index.html', status=200)
