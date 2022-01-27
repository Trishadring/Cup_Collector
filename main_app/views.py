from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Cup
from .forms import UsingForm

# from .models import Cup


class CupCreate(CreateView):
    model = Cup
    fields = '__all__'
    success_url = '/cats/'

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
    using_form = UsingForm()
    return render(request, 'cups/detail.html', {
        'cup': cup, 'using_form': using_form
    })


def add_use(request, cup_id):
   # create a ModelForm instance using the data in request.POST
    form = UsingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_use = form.save(commit=False)
        new_use.cup_id = cup_id
        new_use.save()
    return redirect('detail', cup_id=cup_id)
