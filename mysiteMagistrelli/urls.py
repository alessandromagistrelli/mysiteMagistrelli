"""mysiteMagistrelli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

#fase 1
#una rotta è una stringa che contiene un pattern url. quando si fa una richiesta django fa partire il primo pattern in urlpatterns. comparando l'url richiesto con ogni pattern finche non trova quello corretto
#quando django trova il pattern corretto chiama la funzione con una HttpRequest.
#l'argomento puo essere passato in un dizionario alla view target
#nominare il tuo url permette di evitare ambiguità in django

#fase 2
#nel file models.py creiamo le classi domanda e scelta, poi aggiungiamo l'applicazione alle app installate nel settings.py, successivamente facciamo le migrazioni per creare il database. successivamente apriamo la shell e digitando i comandi inseriamo all'interno del database le domande e le risposte, infine aggiorniamo le funzioni question e choice nel models e creiamoo il superuser admin che potrà gestire il server e gli utenti

#fase 3
#nelle views andiamo ad aggiungere le funzioni detail results e vote e successivamente le importiamo nella urls.py, successivamente modifichiamo la funzione index nel file views per poi andare a sviluppare la pagina index.html. nel file views andiamo inoltre a realizzare il la vista in caso di errore 404 per spiegare all'utente in che pagina recarsi. infine andiamo ad aggiornare il file urls.py per includere tutte le funzioni collegate alla relativa pagina

#fase 4
#andiamo a modificare la pagina detail.html, successivamente nelle views andiamo ad aggiornare  le funzioni vote e result e creo la pagina results.html. infine nella pagina views.py creo le classi IndexView, DetailView e ResultsView








