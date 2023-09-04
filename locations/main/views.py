from django.shortcuts import render, redirect
from .models import Location, Comment
from django.http import JsonResponse

def index(request):
    locations = Location.objects.all()
    return render(request, 'index.html', {
        'locations': locations
    })

def add_location(request):
    Location.objects.create(name=request.POST['name'])
    return redirect('/')

def like(request, id):
  location = Location.objects.get(id=id)
  location.likes += 1
  location.save()
  return redirect('/')

def dislike(request, id):
  location = Location.objects.get(id=id)
  location.dislikes += 1
  location.save()
  return redirect('/')

def comment(request):
    c = Comment()
    c.location_id = request.POST['location_id']
    c.text = request.POST['text']
    c.save()
    return JsonResponse({
        'message': 'Comment added'
    })