from django.shortcuts import render
from django.conf import settings
import requests
from datetime import datetime,timezone, timedelta
# Create your views here.
def weather(request):
    data=None
    d={}
    if request.method == "POST":
        city=request.POST.get('city')
        data=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.API_KEY}').json()
        # print(data)
        for i,j in data.items():
            if i=="coord":
                for k,v in j.items():
                    if k=='lon':
                        d['longitude']=v
                    elif k=='lat':
                        d['latitude']=v
            elif i=='weather':
                for k in j:
                    d['weather']=k['main']
                    d['description']=k['description']
            elif i=='main':
                for k,v in j.items():
                    if k in ['temp', 'feels_like', 'temp_min', 'temp_max']:
                        d[k]=round(v-273.5,1)
                    elif k in ['pressure', 'humidity', 'sea_level']:
                        d[k]=v
            elif i=='visibility':
                d['visibility']=j
            elif i=='wind':
                d['wind_speed']=j['speed']
            elif i=='sys':
                d['country']=j['country']
                ist = timezone(timedelta(hours=5, minutes=30))
                sunrise = datetime.fromtimestamp(j['sunrise'], ist)
                sunset = datetime.fromtimestamp(j['sunset'], ist)
                d['sunrise'] = sunrise.strftime("%I:%M:%S %p")
                d['sunset'] = sunset.strftime("%I:%M:%S %p")
            elif i == 'name':
                d['city'] = j
    return render(request,'weather.html',{'data':d})