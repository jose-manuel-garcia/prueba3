from django.shortcuts import render
from aplicacion.models import *
# Create your views here

def usuarios_view(request):
    tweets = []
    retweets = []
    error = ""
    usuario = Usuario.objects.filter(id = 1002)[0]
    tweets = list(Tweet.objects.filter(usuario = usuario))
    

    if len(tweets) <= 0:
        error = "no hay tweets de este usuario"
    else:
        for ret in tweets:
            if (Retweet.objects.filter(tweet = ret)) :
                retweets.append(Retweet.objects.filter(tweet = ret)[0])
    
        print(retweets)
        if len(retweets) <= 0:
            error = "no hay retweets"
    #se evitan repeticiones
    
    context = {
        'username':usuario.username,
        'retweets': retweets,
        'error': error
    }
    return render(request ,'usuario.html', context= context)