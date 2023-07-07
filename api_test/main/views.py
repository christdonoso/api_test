from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .api_request import *
# Create your views here.


def index(request):
    """
    Esta view redirecciona a cualquier persona que visite el index 
    a la pagina de longin
    """
    return redirect('accounts/login')


@login_required
def main(request):

    """
    Procesa la peticion del usuario dependiendo del metodo

    In GET: retorna la pagina vacia
    IN POST: toma el input de la ciudad y se lo pasa a las funciones 
    """

    if request.method == 'POST':
        city = request.POST['city']
        coord= get_lat(city)
        if coord == None:
            return render(request, 'main2.html',{'msje':True})
        else:
            weather = get_weather(coord['latitud'], coord['longitud'])
            info = coord | weather
            print(info)
            return render(request, 'main.html', {'info':info})
    else:
        return render(request, 'main2.html')
    


