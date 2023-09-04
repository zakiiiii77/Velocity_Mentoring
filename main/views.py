import json
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

def like_location(request, location_id):
    location = Location.objects.get(id=location_id)
    location.likes += 1
    location.save()
    return JsonResponse({'likes': location.likes})

def dislike_location(request, location_id):
    location = Location.objects.get(id=location_id)
    location.dislikes += 1
    location.save()
    return JsonResponse({'dislikes': location.dislikes})

def add_comment(request, location_id):
    if request.method == "POST":
        data = json.loads(request.body)
        location = Location.objects.get(id=location_id)
        comment = Comment.objects.create(location=location, text=data["text"])
        return JsonResponse({"comment_id": comment.id})

def index(request):
  locations = Location.objects.all()

  for location in locations:
    location.comments = location.comment_set.all()

  context = {
    'locations': locations
  }
  return render(request, 'index.html', context)