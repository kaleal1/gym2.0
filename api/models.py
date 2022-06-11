from django.db import models


# Create your models here.
class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=50, verbose_name= 'Username')
    Usernombre = models.CharField(max_length=50, verbose_name='Nombre')
    UserHeight = models.FloatField(verbose_name='Altura')
    UserWeight = models.FloatField(verbose_name='Peso')

    def __str__(self):
        fila = "Username: " + self.Username + " - " + "Nombre: " + self.Usernombre
        return fila


class Excercise(models.Model):
    ExcerciseId = models.AutoField(primary_key=True)
    ExcerciseName = models.CharField(max_length=50, verbose_name='Nombre')
    ExcerciseImage = models.ImageField(upload_to='images/', verbose_name='Imagen', null=True)
    ExcerciseDescription = models.TextField(verbose_name='Descripcion')
    ExcerciseMuscle = models.CharField(max_length=50, verbose_name='Musculo')

    def __str__(self):
        datos = "Nombre: " + self.ExcerciseName + " - " + "Musculo: " + self.ExcerciseMuscle
        return datos

    def delete(self, using=None, keep_parents=False):
        self.ExcerciseImage.storage.delete(self.ExcerciseImage.name)
        super().delete()