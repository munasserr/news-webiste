from django.shortcuts import render
import requests , random

API_KEY = "a3343bd6c2834603a012551717f67c2b"

def home(request):
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
    country = request.GET.get('country')
    category = request.GET.get('category')
    if country :
        url= f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    articles = data['articles']


    context = {
        'art' : articles,
    } 

    return render(request , 'index.html' , context)