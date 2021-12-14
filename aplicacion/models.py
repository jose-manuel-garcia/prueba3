from django.db import models
from django.db.models.expressions import ValueRange
from django.db.models.fields import EmailField, TimeField
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

#Modelo usuario
class Usuario(models.Model):
    """
    Modelo que representa un usuario.
    """
    # fields
    username = models.CharField(max_length=200, help_text='nombre de usuario')
    
    
    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return "%s" % (self.username)

#modelo
class Tweet(models.Model):
    """
    Modelo que representa un tweet.
    """

    texto = models.CharField(max_length=1000, help_text='texto del tweet')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, related_name='usuario')
    #seleccionamos auto_now_add para que se genere la fecha automaticamente el crear el tweet, lo que facilita nuestro codigo
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
   
    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        """
        return "%s %s" % (self.texto, self.fecha)

class Retweet(models.Model):
    """
    Modelo que representa un retweet.
    """
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, null=True, related_name='tweet')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, related_name='usuarioTweet')
    #seleccionamos auto_now_add para que se genere la fecha automaticamente el crear el tweet, lo que facilita nuestro codigo
    fechaDeRetweet = models.DateTimeField(auto_now_add=True, blank=True)
   