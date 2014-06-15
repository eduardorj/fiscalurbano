from app.fiscalizacao.models import Relato, Tag
from django.conf import settings
from django.shortcuts import render_to_response, render
from django.contrib.gis.shortcuts import render_to_kml

def homepage(request):
	context = {'MEDIA_URL': settings.MEDIA_URL}
	return render_to_response('index.html', context)

def generateKml(request):
	context = {'MEDIA_URL': settings.MEDIA_URL}
	relatos = Relato.objects.all() 
	return render_to_kml('location.html', {'relatos':relatos})

def tags(request):
    tags = Tag.objects.all()
    return render(request, 'tags.html', {'tags': tags})