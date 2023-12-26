from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import Movieform


# Create your views here.
def moviefun(request):
    movie = Movie.objects.all()
    context = {'movie_list': movie}
    return render(request, 'index.html', context)


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'details.html', {'movie': movie})


def addmovie(request):
    if request.method == "POST":
        name = request.POST.get('moviename', )
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        image = request.FILES['image']
        movie = Movie(name=name, desc=desc, year=year, img=image)
        movie.save()
    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    forms = Movieform(request.POST or None, request.FILES, instance=movie)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': forms, 'movi': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')
