from django.shortcuts import render, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.
def MovieFlix(request):
    return render(request, "MovieFlix.html")
def index(request):
    return render(request, "login.html")

def ComingSoon(request):
    return render(request, "ComingSoon.html")

def topMovies(request):
    return render(request, "topMovies.html")

def login(request):
    return render(request, "login.html")
def moviedetail(request, movie_slug):
    movie = get_object_or_404(Movie, slug=movie_slug)
    return render(request, 'moviedetail.html', {'movie': movie})

def cocktail(request):
    return render(request, "cocktail.html")
def moviedetail(request, movie_slug):
    
    movie = get_object_or_404(Movie, slug=movie_slug)
    return render(request, 'moviedetail.html', {'movie': movie})

def arrival(request):
    return render(request, "arrival.html")

def interstellar(request):
    return render(request, "interstellar.html")

def johnwick(request):
    return render(request, "johnwick.html")

def jurassicpark(request):
    return render(request, "jurassicpark.html")

def kalki(request):
    return render(request, "kalki.html")

def madmax(request):
    return render(request, "madmax.html")

def missionimpossible(request):
    return render(request, "missionimpossible.html")

def martian(request):
    return render(request, "martian.html")

def maverick(request):
    return render(request, "maverick.html")

def spacejam(request):
    return render(request, "spacemam.html")

def thematrixrevolutions(request):
    return render(request, "thematrixrevolutions.html")

def war(request):
    return render(request, "war.html")

def yodha(request):
    return render(request, "yodha.html")


from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        
        messages.success(request, 'Login successful')
    return render(request, 'login.html')
def review(request):
    return render(request, "review.html")
def reveiw(request):
    return render(request, "reveiw.html")
def housefull5(request):
    return render(request, 'comming/housefull5.html')
def avtaar(request):
    return render(request, 'comming/avtaar.html')
def thuglife(request):
    return render(request, 'comming/thuglife.html')
def baaghi(request):
    return render(request, 'comming/baaghi.html')

from django.shortcuts import render
from .models import Movie  

def search_movies(request):
    query = request.GET.get('q', '')  
    if query:
        
        movies = Movie.objects.filter(title__icontains=query)  
    else:
        movies = Movie.objects.all()  

    return render(request, 'your_template.html', {'movies': movies, 'query': query})

def bhoolchukmaaf(request):
    return render(request, 'comming/bhoolchukmaaf.html')
def kantarachapter1(request):
    return render(request, 'comming/kantarachapter1.html')

def F1(request):
    return render(request, 'comming/F1.html')
def jb(request):
    return render(request, 'comming/jb.html')
def kuberaa(request):
    return render(request, 'comming/kuberaa.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def cocktail(request):
    return render(request, 'moviedetail/cocktail.html')
def pari(request):
    return render(request, 'moviedetail/pari.html')
def dhamaal(request):
    return render(request, 'moviedetail/dhamaal.html')
def herapherii(request):
    return render(request, 'moviedetail/herapherii.html')
def dostana(request):
    return render(request, 'moviedetail/dostana.html')
def bandbaajabaaraat(request):
    return render(request, 'moviedetail/bandbaajabaaraat.html')
def kalki(request):
    return render(request, 'moviedetail/kalki.html')
def maverick(request):
    return render(request, 'moviedetail/maverick.html')
def yodha(request):
    return render(request, 'moviedetail/yodha.html')
def thematrixresurrections(request):
    return render(request, 'moviedetail/thematrixresurrections.html')
def war(request):
    return render(request, 'moviedetail/war.html')
def dopatti(request):
    return render(request, 'moviedetail/dopatti.html')
def joker(request):
    return render(request, 'moviedetail/joker.html')
def idiots3(request):
    return render(request, 'moviedetail/idiots3.html')
def munjya(request):
    return render(request, 'moviedetail/munjya.html')