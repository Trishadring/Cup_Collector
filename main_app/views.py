from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Cup

# from .models import Cup


class CupCreate(CreateView):
    model = Cup
    fields = '__all__'
    success_url = '/cats/'

cups = [
	
    Cup(id=2, color='red', brand = 'yeti', type ='travel mug', description ="n/a"),
    Cup('white', 'cbs', 'coffee cup', "law and order cup")
]
cups = [
	
    Cup('1', 'red', 'yeti', 'travel mug', "n/a"),
    Cup('white', 'cbs', 'coffee cup', "law and order cup")
]

# Create your views here.
class CupUpdate(UpdateView):
  model = Cup
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['color', 'type', 'description', 'brand']

class CupDelete(DeleteView):
  model = Cup
  success_url = '/cups/'

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    return render(request, 'about.html')


def cup_index(request):
    cups = Cup.objects.all()
    return render(request, 'cups/index.html', {'cups': cups})

def cup_detail(request, cup_id):
  cup = Cup.objects.get(id=cup_id)
  return render(request, 'cups/detail.html', { 'cup': cup })