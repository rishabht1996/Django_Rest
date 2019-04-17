from django.shortcuts import render
from django.http import HttpResponse
from . import forms  # Wheneer there are two files present over the same dir.
from rest_framework import generics
from .models import Signup
from .serializers import SnippetSerializer

# Create your views here.

def index(request):
    return HttpResponse("Hello, I just created My First Application.")

def rishabh(request):
    return HttpResponse("Hello I ma the second Function")

def example(request):
    return HttpResponse("Hello I am an example")


def template_demo(request):
    dict_var= {'random_var':" I am Written in Views.py"}
    return render(request,'firstapp/index.html', context= dict_var)


def form_view(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():  # This is mandatory in Django 2

            print("My_Password = "+form.cleaned_data["password"])  # 1 Way to get values over the terminal
            print(request.POST.get("name")) # 2 Way to get values
            form.save()
            return HttpResponse("Your Values are saved")
        else:
            print(form.errors)
            return render(request, 'firstapp/basic_form.html', {'form': form})
    return render(request,'firstapp/basic_form.html',{'form':form})


class SnippetList(generics.ListCreateAPIView):
    queryset = Signup.objects.all()
    serializer_class = SnippetSerializer



class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Signup.objects.all()
    serializer_class = SnippetSerializer
