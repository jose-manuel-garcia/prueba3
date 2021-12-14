import os
import random
from django.core.management.base import BaseCommand
from aplicacion.models import *


class Command(BaseCommand):
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = """populate database
           """

    def handle(self, *args, **kwargs):
        self.cleanDataBase()
        self.usuarios()
        self.tweets()
        self.retweets()

    def cleanDataBase(self):
        # delete all models stored (clean table)
        # in database
        Usuario.objects.all().delete()
        Tweet.objects.all().delete()
        Retweet.objects.all().delete()

    def usuarios(self):
        u1 = Usuario.objects.create(id=1001, username='usuario_01')
        u2 = Usuario.objects.create(id=1002, username='usuario_02')
        u3 = Usuario.objects.create(id=1003, username='usuario_03')

    def tweets(self):
        t1 = Tweet.objects.create(id=1001, texto='texto de mensaje 01',
                                  usuario=Usuario.objects.filter(id=1002)[0], fecha='05-01-2021')
        t2 = Tweet.objects.create(id=1002, texto='texto de mensaje 02',
                                  usuario=Usuario.objects.filter(id=1001)[0], fecha='10-01-2021')
        t3 = Tweet.objects.create(id=1003, texto='texto de mensaje 03',
                                  usuario=Usuario.objects.filter(id=1002)[0], fecha='12-01-2021')
        t4 = Tweet.objects.create(id=1004, texto='texto de mensaje 04',
                                  usuario=Usuario.objects.filter(id=1002)[0], fecha='15-01-2021')

    def retweets(self):
        rt1 = Retweet.objects.create(id=1001, usuario=Usuario.objects.filter(id=1001)[
                                     0], tweet=Tweet.objects.filter(id=1003)[0], fechaDeRetweet='05-01-2021')
        rt2 = Retweet.objects.create(id=1002, usuario=Usuario.objects.filter(id=1001)[
                                     0], tweet=Tweet.objects.filter(id=1001)[0], fechaDeRetweet='05-01-2021')
        rt3 = Retweet.objects.create(id=1003, usuario=Usuario.objects.filter(id=1002)[
                                     0], tweet=Tweet.objects.filter(id=1003)[0], fechaDeRetweet='05-01-2021')
        rt4 = Retweet.objects.create(id=1004, usuario=Usuario.objects.filter(id=1003)[
                                     0], tweet=Tweet.objects.filter(id=1003)[0], fechaDeRetweet='05-01-2021')
