from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Excercise, Routine
from .forms import UserForm, ExcerciseForm, RoutineForm

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

#vistas para usuario
def user(request):
    user = User.objects.all()
    return render(request, 'User/index.html', {'user': user})
def crearuser(request):
    userformulario = UserForm(request.POST or None)
    return render(request, 'User/crear.html', {'userformulario': userformulario})
def editaruser(request):
    return render(request, 'User/editar.html')

#vistas para ejercicos
def excersice(request):
    excersice = Excercise.objects.all()
    return render(request, 'excersice/index.html', {'excersice': excersice})
def crearexcersice(request):
    excersiceformulario = ExcerciseForm(request.POST or None, request.FILES or None)
    if excersiceformulario.is_valid():
        excersiceformulario.save()
        return HttpResponse('Guardado')
    return render(request, 'excersice/crear.html', {'excersiceformulario': excersiceformulario})
def editarexcersice(request):
    return render(request, 'excersice/editar.html')


def routine(request):
    routine = Routine.objects.all()
    return render(request, 'routine/index.html', {'routine': excersice})
def crearroutine(request):
    routineformulario = ExcerciseForm(request.POST or None, request.FILES or None)
    if routineformulario.is_valid():
        routineformulario.save()
        return HttpResponse('Guardado')
    return render(request, 'routine/crear.html', {'routineformulario': routineformulario})
def editarroutine(request):
    return render(request, 'routine/editar.html')