import requests
from django.shortcuts import render

def index(request):
	appid = 'a873b03eb69e861de4fac07c1a97113a'
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + appid

	city = 'London'
	res = requests.get(url.format(city))
	print(res.text)

	return render(request, 'weather/index.html')