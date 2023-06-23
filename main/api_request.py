"""
Este script se encarga de manejar las peticiones a la api de openweathermap
https://openweathermap.org/api, la que disponibiliza varios endpoints gratuitis
para obtener el estado actual del clima en varias ciudades, el manejo de la clave de la api
se realiza mediante un archivo externo protegido. el script cuenta primero con una lambda
que realiza convercion de unidades, 2 funciones que realizan el manejo de las peticiones a los
diferentes endpoints para obtener la informacion necesaria.
"""

import requests
from decouple import config


API_KEY = config('API_KEY')
to_celcius = lambda x : round(float(x) - 273.15, 1)
 

def get_lat(city:str)-> dict | None:

    """_summary_
    esta funcion recibe el nombre de una ciudad como parametro, realiza 
    una peticion get a la api de openweathermap.
    Args:
        city (str): el nombre de la ciudad
    Returns:
        dict | None: None si la ciudad no existe
                     Dict {'name':name,'latitud':lat,'longitud': lon,'counyt':country}
    """

    api_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API_KEY}'
    r = requests.get(api_url)

    if r.text == '[]' or city == '':
        return None
    else:
        name = r.json()[0]['name'] 
        country = r.json()[0]['country']
        lat = r.json()[0]['lat']
        lon =  r.json()[0]['lon']
        return {'name':name,'latitud':lat,'longitud': lon,'country':country}
        

def get_weather(lat:str,lon:str) -> dict:

    """_summary_
    Esta funcion recibe la latitud y longitud de la ciudad que se desea buscar y 
    realiza la consulta en la api de openweathermap.
    Args:
        lat (str): latitud de la ciudad
        lon (str): longitud de la ciudad
    Returns:
        dict: un diccionario con los parametros deseados
        {'id': 741, 'main': 'Fog', 'description': 'bruma', 'icon': '50d', 
        'img': 'http://openweathermap.org/img/wn/50d@2x.png', 'temp': 288.15, 
        'feels_like': 288.16, 'temp_min': 287.35, 'temp_max': 288.15, 'pressure': 1020, 
        'humidity': 94, 'celcius': 15.0, 'min': 14.2, 'max': 15.0}
    """

    api_descr = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&lang=es'
    r = requests.get(api_descr).json()
    weather = r['weather'][0] 
    # respuesta: {'id': 804, 'main': 'Clouds', 'description': 'nubes', 'icon': '04d'}
    weather['img'] =f'http://openweathermap.org/img/wn/{weather["icon"]}@2x.png'
    main = r['main'] 
    #respuest: {'temp': 288.7, 'feels_like': 287.85, 'temp_min': 287.09, 'temp_max': 289.44, 'pressure': 1015, 'humidity': 59, 'sea_level': 1015, 'grnd_level': 998}
    main['celcius'] = to_celcius(main['temp'])
    main['min'] = to_celcius(main['temp_min'])
    main['max'] = to_celcius(main['temp_max'])
    # http://openweathermap.org/img/wn/"+ iconcode + @2x".png"  --> img url
    return weather | main 


if __name__ == '__main__':
    coord = get_lat('quilpue')
    if coord == None:
        print('no viene nada')
    else:
        print(coord)
        g = get_weather(coord['latitud'], coord['longitud'])
        print(g)

