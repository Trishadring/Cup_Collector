from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Cup, Sticker
from .forms import UsingForm

class CupCreate(CreateView):
		model = Cup
		fields = '__all__'
		success_url = '/cups/'

class CupUpdate(UpdateView):
		model = Cup
		# Let's disallow the renaming of a cup by excluding the name field!
		fields = ['color', 'type', 'description', 'brand']


class CupDelete(DeleteView):
		model = Cup
		success_url = '/cups/'


def home(request):
		return render(request, 'home.html')


def about(request):
		return render(request, 'about.html')


def cup_index(request):
		cups = Cup.objects.all()
		return render(request, 'cups/index.html', {'cups': cups})


def cup_detail(request, cup_id):
		cup = Cup.objects.get(id=cup_id)
		stickers_cup_no_have = Sticker.objects.exclude(
			id__in=cup.stickers.all().values_list('id'))
		using_form = UsingForm()
		return render(request, 'cups/detail.html', {
				'cup': cup, 'using_form': using_form,
				'stickers': stickers_cup_no_have
		})


def add_use(request, cup_id):
		# create a ModelForm instance using the data in request.POST
		form = UsingForm(request.POST)
		# validate the form
		if form.is_valid():
				# don't save the form to the db until it
				# has the cup_id assigned
				new_use = form.save(commit=False)
				new_use.cup_id = cup_id
				new_use.save()
		return redirect('detail', cup_id=cup_id)

def assoc_sticker(request, cup_id, sticker_id):
	# Note that you can pass a sticker's id instead of the whole object
	Cup.objects.get(id=cup_id).stickers.add(sticker_id)
	return redirect('detail', cup_id=cup_id)


class StickerList(ListView):
		model = Sticker


class StickerDetail(DetailView):
		model = Sticker


class StickerCreate(CreateView):
		model = Sticker
		fields = '__all__'


class StickerUpdate(UpdateView):
		model = Sticker
		fields = ['name', 'color']


class StickerDelete(DeleteView):
		model = Sticker
		success_url = '/stickers/'