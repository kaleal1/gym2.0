from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import User, Excercise, Routine
from .forms import UserForm, ExcerciseForm, RoutineForm


# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')


# vistas para usuario
def users(request):
    users = User.objects.all()
    return render(request, 'User/index.html', {'users': users})


def crearusers(request):
    userformulario = UserForm(request.POST or None)
    if userformulario.is_valid():
        userformulario.save()
    return render(request, 'User/crear.html', {'userformulario': userformulario})


def editarusers(request):
    return render(request, 'User/editar.html')


# vistas para ejercicos
def excercises(request):
    excercises = Excercise.objects.all()
    return render(request, 'excercise/index.html', {'excercises': excercises})


def crearexcercises(request):
    excerciseformulario = ExcerciseForm(request.POST or None, request.FILES or None)
    if excerciseformulario.is_valid():
        excerciseformulario.save()
        return HttpResponse('Guardado')
    return render(request, 'excercise/crear.html', {'excerciseformulario': excerciseformulario})


def editarexcercises(request):
    return render(request, 'excercise/editar.html')


def eliminarexcercises(request, id):
    excercise = Excercise.objects.get(id=id)
    excercise.delete()
    return redirect('excercises')


def routines(request):
    rout = Routine.objects.get(id=1)
    excercises = rout.excercise.all()
    return render(request, 'routine/index.html', {'excercises': excercises})

def eliminarexcercisesrout(request, id):
    routine = Routine.objects.get(id=1)
    excercises = routine.excercise.all()
    exBorrar = excercises.get(id=id)
    exBorrar.delete()                                    #listo todos los excercise de la rutina
    return redirect('routines')

def agregarexcercise(request,id):
    excercise = Excercise.objects.get(id=id)
    routine =Routine.objects.get(id=1)
    routine.excercise.add(excercise)
    return redirect('excercises')




# def crearroutines(request):
#     routineformulario = ExcerciseForm(request.POST or None, request.FILES or None)
#     if routineformulario.is_valid():
#         routineformulario.save()
#         return HttpResponse('Guardado')
#     return render(request, 'routine/crear.html', {'routineformulario': routineformulario})


def editarroutines(request):
    return render(request, 'routine/editar.html')


def showlist(request):
    results = Excercise.objects.all
    return render(request, "Routine/form.html", {"Excercise": results})


def addexcercise(request, id):
    productobj = get_object_or_404(Excercise, id=id)
    routinecart = Routine()
    routinecart.excercise.add(productobj)
    return render(request, 'Routine/index.html')
