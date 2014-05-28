from app.fiscalizacao.models import Relato
from django.conf import settings
from django.shortcuts import render_to_response
from django.contrib.gis.shortcuts import render_to_kml

def homepage(request):
	context = {'MEDIA_URL': settings.MEDIA_URL}
	return render_to_response('index.html', context)

def generateKml(request):
	context = {'MEDIA_URL': settings.MEDIA_URL}
	relatos = Relato.objects.all() 
	return render_to_kml('location.html', {'relatos':relatos})

def save_events_json(request):
	print "entrou"
	if request.is_ajax():
		if request.method == 'POST':
			print 'Raw Data: "%s"' % request.raw_post_data
			return HttpResponse("OK")