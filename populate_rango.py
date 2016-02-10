import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practica_django.settings')

import django
django.setup()

from rango.models import Bares, Tapas


def populate():
    bar_Ali = aniadeBar("Aliatar",direccion='Calle picasso, 1',visitas=1)

    aniadeTapa(nombrebar=bar_Ali,
        nombre="carne al ajillo",
        votos=2)

    aniadeTapa(nombrebar=bar_Ali,
        nombre="albondigas con tomate",
        votos=1)

    aniadeTapa(nombrebar=bar_Ali,
        nombre="pizza 4 quesos",
        votos=4)
    
    bar_Juan = aniadeBar("Juan",direccion='Calle navas, 2',visitas=3)

    aniadeTapa(nombrebar=bar_Juan,
        nombre="Carne en salsa",
        votos=2)

    aniadeTapa(nombrebar=bar_Juan,
        nombre="Pizza",
        votos=1)

    aniadeTapa(nombrebar=bar_Juan,
        nombre="Montadito Lomo",
        votos=4)

    bar_Marino = aniadeBar("Marino",direccion='Calle navas, 2',visitas=2)

    aniadeTapa(nombrebar=bar_Marino,
        nombre="Pollo Asado",
        votos=2)

    aniadeTapa(nombrebar=bar_Marino,
        nombre="Paella",
        votos=1)

    aniadeTapa(nombrebar=bar_Marino,
        nombre="Arroz 3 delicias",
        votos=4)
    
    bar_Yucas = aniadeBar("Yucas",direccion='Calle navas, 2',visitas=10)

    aniadeTapa(nombrebar=bar_Yucas,
        nombre="Hamburguesa",
        votos=2)

    aniadeTapa(nombrebar=bar_Yucas,
        nombre="Sandwich",
        votos=1)

    aniadeTapa(nombrebar=bar_Yucas,
        nombre="Cazon",
        votos=4)
    
    bar_Palomas = aniadeBar("Palomas",direccion='Calle navas, 2',visitas=5)

    aniadeTapa(nombrebar=bar_Palomas,
        nombre="Hamburguesa con queso",
        votos=2)

    aniadeTapa(nombrebar=bar_Palomas,
        nombre="Sandwich de pollo",
        votos=1)

    aniadeTapa(nombrebar=bar_Palomas,
        nombre="Chipirones",
        votos=4)

    # Print out what we have added to the user.
    for c in Bares.objects.all():
        for p in Tapas.objects.filter(nombrebar=c):
            print "- {0} - {1}".format(str(c), str(p))

def aniadeTapa(nombrebar, nombre, votos):
    p = Tapas.objects.get_or_create(nombrebar=nombrebar, nombre=nombre)[0]
    p.votos=votos
    p.save()
    return p

def aniadeBar(nombre, direccion,visitas):
    c = Bares.objects.get_or_create(nombre=nombre)[0]
    c.direccion=direccion
    c.visitas=visitas
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()