from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
def index(request):
    #return HttpResponse('hola mundo')
    #varEstudiante = Estudiante.objects.get(nombres="Valeria", apellidos="Enri" )#.filter
    grupo_1 = Estudiante.objects.filter(grupo=1)

    grupo_4 = Estudiante.objects.filter(grupo=4)


    todos = Estudiante.objects.all()

    #unicos_apellidos = Estudiante.objects.values_list('apellidos', flat=True).distinct()
    #print(unicos_apellidos)
    #rep_apellidos = todos.exclude(apellidos__in = unicos_apellidos.values_list('apellidos', flat=True))
    apd =  Estudiante.objects.values_list('apellidos', flat=True)
    r_apellidos = repetidos(apd.distinct(),  apd)#todos.exclude(id__in=blacklist)
    # And filter the queryset with the new whitelist
    #rep_apellidos = queryset.filter(product_names__in=whitelist).distinct()
    rep_apellidos = todos.filter(apellidos__in = r_apellidos)

    ed = Estudiante.objects.values_list('edad', flat=True)
    r_edad = repetidos(ed.distinct(),  ed)
    #unicos_edad = Estudiante.objects.values('edad').distinct()
    rep_edad = todos.filter(edad__in = r_edad)

    rep_edad_3 = rep_edad.filter(grupo=3)
    #print(varEstudiante)
    return render(request, 'index.html', {'grupo_1':grupo_1,
                                            'grupo_4':grupo_4,
                                            'rep_apellidos': rep_apellidos,
                                            'rep_edad': rep_edad,
                                            'rep_edad_3': rep_edad_3,
                                            'todos':todos})
def repetidos(l_u,l):
    uniq = {l_u[i]: 0 for i in range(0, len(l_u))}
    repetidos =[]
    for i in l:
        uniq[i] = uniq[i] + 1
        if uniq[i] > 1:
            repetidos.append(i)
    return repetidos