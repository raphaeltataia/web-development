from django.shortcuts import render

# Developed by @raphaeltataia

from django.http import HttpResponse

def index(request):
	return HttpResponse("Alô Mundo!")
