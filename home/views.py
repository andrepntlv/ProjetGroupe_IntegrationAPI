from django.shortcuts import render
import finnhub
# Setup client
finnhub_client = finnhub.Client(api_key="c0db36n48v6vf7f7l8mg")
# Create your views here.
def home(request):
    finnhub_client = finnhub.Client(api_key="c0db36n48v6vf7f7l8mg")

    # Entreprise proposé
    company_recommande = ["TSLA", "AMZN", "AAPL", "MFST", "NFLX", "FB"]
    list_recomande = []

    for ticker in company_recommande:
        if not len(finnhub_client.company_profile2(symbol=ticker)) == 0:
            information = []
            information.append(finnhub_client.company_profile2(symbol=ticker)["ticker"])
            information.append(finnhub_client.company_profile2(symbol=ticker)["name"])
            information.append(finnhub_client.company_profile2(symbol=ticker)["marketCapitalization"])
            information.append(finnhub_client.company_profile2(symbol=ticker)["shareOutstanding"])
            information.append(finnhub_client.company_profile2(symbol=ticker)["logo"])
            information.append(finnhub_client.quote(ticker)["c"])
            list_recomande.append(information)


    # Classement
    liste = finnhub_client.stock_symbols('US')[0:5]
    liste_company = []

    for key in liste:
        ticker = key["displaySymbol"]
        if not len(finnhub_client.company_profile2(symbol=ticker)) == 0:
            information = []
            information.append(finnhub_client.company_profile2(symbol=ticker)["ticker"])
            information.append(finnhub_client.company_profile2(symbol=ticker)["name"])
            information.append(finnhub_client.company_profile2(symbol=ticker)["marketCapitalization"])
            information.append(finnhub_client.company_profile2(symbol=ticker)["shareOutstanding"])
            information.append(finnhub_client.quote(ticker)["c"])
            liste_company.append(information)


    context = {
        'list_recomande' : list_recomande,
        'liste_company' : liste_company,
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