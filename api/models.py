from django.db import models, connections

# Create your models here.
from django.forms import ModelForm


class User(models.Model):
   # objects = None
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, verbose_name='Username')
    name = models.CharField(max_length=50, verbose_name='Nombre')
    height = models.FloatField(verbose_name='Altura')
    weight = models.FloatField(verbose_name='Peso')

    def __str__(self):
        fila = "Username: " + self.username + " - " + "Nombre: " + self.name
        return fila


class Excercise(models.Model):
    #objects = None
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Nombre')
    image = models.ImageField(upload_to='images/', verbose_name='Imagen', null=True)
    description = models.TextField(verbose_name='Descripcion')
    muscle = models.CharField(max_length=50, verbose_name='Musculo')

    def __str__(self):
        datos = "Nombre: " + self.name + " - " + "Musculo: " + self.muscle
        return datos

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    class Meta:
        db_table = 'api_excercise'


class Routine(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Nombre Rutina')
    excercise = models.ManyToManyField(Excercise)

    class Meta:
        db_table = 'api_routine'

# class RoutineExcercise(models.Model):
#     Excercise = models.ForeignKey(Excercise, on_delete=models.CASCADE)
#     Routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
#     Description = models.TextField()
#
#     class Meta:
#         db_table = 'api_routineexcercise'


# class History(models.Model):
#     id = models.AutoField(primary_key=True)
#     UserId = models.ForeignKey(User, on_delete=models.CASCADE)
#     RoutineId = models.ForeignKey(Routine, on_delete=models.CASCADE)
#     Usernombre = models.CharField(max_length=50, verbose_name='Nombre')
#     HistoryWeight = models.FloatField(verbose_name='Peso')
#     HistoryDate = models.DateField(auto_now_add=True, verbose_name='Fecha')
