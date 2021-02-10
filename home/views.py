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

def detail(request, ticker):
    dicoCompanyProfile = finnhub_client.company_profile2(symbol=ticker)

    if len(dicoCompanyProfile) == 0:
        return render(request, 'home/detail.html')

    context = {
        "name" : dicoCompanyProfile["name"],
        "logo" : dicoCompanyProfile["logo"],
        "ticker": dicoCompanyProfile["ticker"],
        "country": dicoCompanyProfile["country"],
        "finnhubIndustry": dicoCompanyProfile["finnhubIndustry"],
        "ipo" : dicoCompanyProfile["ipo"],
        "marketCapitalization": dicoCompanyProfile["marketCapitalization"],
        "weburl" : dicoCompanyProfile["weburl"],


    }

    return render(request, 'home/detail.html', context)