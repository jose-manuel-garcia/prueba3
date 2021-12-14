from django.db.models.query import QuerySet
from django.test import TestCase
# Create your tests here.

from .models import *
from .management.commands.poblar import Command





class AuthorModelTest(TestCase):

    def tearDown(self):

        print('eliminacion registros:')
        print('eliminado socios:')
        Usuario.objects.all().delete()
        print('eliminado pistas:')
        Tweet.objects.all().delete()
        print('eliminado reservas:')
        Retweet.objects.all().delete()
    

    @classmethod
    def setUpTestData(cls):
        
        u2 = Usuario.objects.create(id=1001, username='usuarioTw1')
        u3 = Usuario.objects.create(id=1002, username='usuarioTw2')
        t1 = Tweet.objects.create(id=1001, texto='texto del tweet 01',
                                  usuario=Usuario.objects.filter(id=1001)[0], fecha='25-01-2021')

       
        
        rt1 = Retweet.objects.create(id=1001, usuario=Usuario.objects.filter(id=1001)[
                                     0], tweet=Tweet.objects.filter(id=1001)[0], fechaDeRetweet='25-01-2021')
    def test_url(self):
        
        resp = self.client.get('/aplicacion/usuario/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'usuario.html')
        self.assertEqual(len(list(resp.context['retweets'])), 0)
        self.assertEqual(resp.context['error'], 'no hay tweets de este usuario')

        # se crean los nuevos registros:


    
