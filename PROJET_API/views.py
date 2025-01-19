from dbm import error

from django.contrib import messages

from django.shortcuts import render, redirect
import requests
API_KEY="ba86589525e79a95c340c6bd6c6fa33d"


def meteo_information(request):
    if request.method=="POST":
      city=request.POST.get("city")

      if city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
           final = []
           response_final = response.json()
           temperature = response_final['main']['temp']
           temp_celsius =int (temperature - 273.15)
           final.append(temp_celsius)
           meteo_ambiante = response_final['weather'][0]['description']
           final.append(meteo_ambiante)
           vent = response_final['wind']['speed']
           final.append(vent)
           return  render(request,"templates.html",context={"response_fin":final})
        else:
           return render(request, "templates.html", {"error": "Erreur lors de l'accès aux données météo."})
    return render(request,"templates.html")

