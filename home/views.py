from django.shortcuts import render
import finnhub
# Setup client
finnhub_client = finnhub.Client(api_key="c0db36n48v6vf7f7l8mg")
# Create your views here.
def home(request):
    listeAction = (finnhub_client.stock_symbols('US')[0:10])
    cle=listeAction[0]

    context={
        "listeAction":listeAction,
        "cle":cle,
    }
    return render(request, 'home/accueil.html',context)