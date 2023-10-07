from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#imported functions
from .service.inference.test import (
    test,

    # other functions from this file
    openai_string_response
)

def home(request):
    return HttpResponse("Hello, World!")

def room(request):
    # RETURN ROOM.HTML
    return render(request, "room.html")

def test_func(request):
    # RETURN TEST FUNCTION
    return HttpResponse(test())


#create a function that takes in a prompt and returns a response frmo a form submission
def get_response(request):
    #get the prompt from the form submission
    prompt = request.POST.get('prompt', None)
    #get the response from the openai api
    response = openai_string_response(prompt)
    #return the response
    return HttpResponse(response)