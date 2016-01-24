from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from smr.models import Movie
from django.template import loader, RequestContext
from smr.serializers import MovieSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def home(request):
	return render(request,'home.html')

	
def list(request):
	movie_list = Movie.objects.all()
	template = loader.get_template('moovie.html')
	context = RequestContext(request, {'movie_list': movie_list,})
	return HttpResponse(template.render(context))

def detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'details.html', {'movie': movie})

@csrf_exempt
def movie_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def movie_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(movie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        movie.delete()
        return HttpResponse(status=204)