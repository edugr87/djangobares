from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rango.models import Bares, Tapas
from rango.forms import BaresForm,TapasForm
from django.contrib.auth.decorators import login_required

def decode_url(str):
        return str.replace('_', ' ')

def index(request):
    #return HttpResponse("Rango says hey there world!")
    Bares_list = Bares.objects.order_by('-nombre')
    context_dict = {'bares': Bares_list}

    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)

def bares(request, bar_name_slug):
    context_dict = {}
    
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        bar = Bares.objects.get(slug=bar_name_slug)
        context_dict['bar_nombre'] = bar.nombre
        context_dict['bar_direccion'] = bar.direccion
        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        tapas = Tapas.objects.filter(nombrebar=bar)

        # Adds our results list to the template context under name pages.
        context_dict['tapas'] = tapas
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['bar'] = bar
        
        bar.visitas+=1
        bar.save()
        
    except Bares.DoesNotExist:
    # We get here if we didn't find the specified category.
    # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'rango/bar.html', context_dict)
    
def about(request):
    return render(request,'rango/about.html')

@login_required
def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = BaresForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = BaresForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})

@login_required
def add_page(request, bar_name_slug):
    
    try:
		bar = Bares.objects.get(slug=bar_name_slug)
    except bar.DoesNotExist:
		bar = None
        
    if request.method == 'POST':
        form = TapasForm(request.POST)
        if form.is_valid():
            if bar:
                tapas = form.save(commit=False)
                tapas.nombrebar = bar
                tapas.votos = 0
                tapas.save()
                # probably better to use a redirect here.
                return bares(request,bar_name_slug)
        else:
            print form.errors
    else:
        form = TapasForm()

    context_dict = {'form':form, 'bar': bar}

    return render(request, 'rango/add_page.html', context_dict)

def reclama_datos (request):
    top_bares = Bares.objects.order_by('-visitas')[:5]
    nombres = []
    visitas = []
    for bar in top_bares:
        nombres.append(bar.nombre)
        visitas.append(bar.visitas)
    datos={'Bares_list':nombres, 'Visit_list':visitas}
    return JsonResponse(datos, safe=False)

def grafica(request):
    Bares_list = Bares.objects.order_by('-nombre')
    context_dict = {'bares': Bares_list}
    return render(request, 'rango/grafica.html',context_dict)