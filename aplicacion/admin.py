from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Usuario)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['username']
    fields = ['username']
    pass


@admin.register(Tweet)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('texto','usuario', 'fecha')
    #la fecha al estar inidicada como un auto_now_add no puede ser modificada desde admin
    fields = ['texto', 'usuario']
    pass


@admin.register(Retweet)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('tweet', 'usuario','fechaDeRetweet' )
    #la fecha al estar inidicada como un auto_now_add no puede ser modificada desde admin
    fields = ['tweet', 'usuario']
    pass
