from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse 
from .models import Persona
# Create your views here.


@csrf_exempt
def get_all(request):
    """    
    Vista que sirve de prueba para ver como funciona una api

    In GET: retorna un json con la informacion de todas las personas 
            en la base de datos
    IN POST: agrega una persona a la base de datos
    """

    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        p = Persona(
            nombre = nombre,
            apellido = apellido
        )
        p.save()
        return HttpResponse('Data Saved')
    else:
        personas = Persona.objects.all()
        json = {}
        for x,p in enumerate(personas):
            json[f'persona {x + 1}'] = {
                'nombre':p.nombre,
                'apellido':p.apellido
            }
        return JsonResponse({'personas':json})
    

@csrf_exempt
def filter(request,name):
    """_summary_

    Vista que resibe un parametro en la url para producir un filtrado
    en la DB
    In GET: retorna un json con la informacion filtrada
    IN POST: No permitido

    Args:
        name (_type_):nombre a buscar

    Returns:
        json 
    """
    if request.method == 'GET':
        persona = Persona.objects.get(nombre = name.capitalize())
        json = {
            'nombre':persona.nombre,
            'apellido':persona.apellido
        }
        return JsonResponse(json)
    else:
        return HttpResponse('POST not allowed')
