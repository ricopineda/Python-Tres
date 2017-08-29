from __future__ import unicode_literals
from models import *
from django.shortcuts import render
import random
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages
from django.utils.crypto import get_random_string
# the index function is called when root is visited
def index(request):

	return render(request,'tres/index.html')

def register(request):

	name = request.POST['name']
	username = request.POST['username']
	password = request.POST['password']

	users = User.objects.filter(username=username)
	if len(users):
		messages.error(request, "This username is taken")
		return redirect('/')
	else:
	
		users = User.objects.create(name=name, username=username, password=password)
		request.session['id'] = users.id
		print request.session['id'] 

		return redirect("/home")

	redirect('/')

def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = User.objects.all().filter(username=username)
		if len(user):
			if user[0].password == password:
				request.session['id'] = user[0].id

				return redirect('/home')
		return redirect ('/')		

def logout(request):

	request.session['id'] = 0
	return redirect('/')

def home(request):
	user = User.objects.get(id=request.session['id'])
	context = {
	'user': user,
	'place': User.objects.get(id=request.session['id']).created_places.all(),
	'other_place': User.objects.get(id=request.session['id']).joined_places.all(),
	'places': Place.objects.all()
	}

	return render(request, 'tres/home.html', context)

def add(request):
	

	return render(request, 'tres/add.html')


def add_trip(request):
	destination = request.POST['destination']
	description = request.POST['description']
	start = request.POST['start']
	end = request.POST['end']

	Place.objects.create(creator_id=request.session['id'], destination=request.POST['destination'], description=request.POST['description'], travel_start=request.POST['start'], travel_end=request.POST['end'])

	return redirect('/home')

def destination(request, id):
	place = Place.objects.get(id=id)
	context ={
	'place': place,
	'others': Place.objects.get(id=id).joiner.all()
	}

	return render(request, 'tres/destination.html', context)


def join(request, id):
	
	Place.objects.get(id=id).joiner.add(User.objects.get(id=request.session['id']))

	return redirect('/home')



























