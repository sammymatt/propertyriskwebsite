from django.http import HttpResponse
from django.shortcuts import render

# Views
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    #return render(request, 'proprisk/index.html')