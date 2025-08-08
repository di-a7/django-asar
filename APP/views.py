from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
   return HttpResponse("<h1>Welcome<h1>")

def home(request):
   people = [
      {"name": "Alice Johnson", "age": 15, "address": "123 Maple Street, Springfield"},
      {"name": "Bob Smith", "age": 4, "address": "456 Oak Avenue, Rivertown"},
      {"name": "Catherine Lee", "age": 22, "address": "789 Pine Road, Lakeside"},
      {"name": "David Kim", "age": 50, "address": "321 Birch Lane, Hillview"},
      {"name": "Emily Davis", "age": 30, "address": "654 Cedar Street, Brookville"}
   ]

   context = {
      "title":"Home",
      "heading":"Welcome home",
      "paragraph": "This is home page",
      "people": people
   }
   return render(request, 'home.html', context)

# home, contact, about_us