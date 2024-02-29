#!/usr/bin/python3
'''API REST server.'''
from fastapi import FastAPI
from datetime import datetime
import requests

app = FastAPI()

# Obtenha e ensira suas chaves API aqui
API_KEYS = {
    "openwhether" : ""  # from <https://api.exchangerate-api.com/>
}

@app.get('/')
def read_root():
    return {
        'message': 'Bem-vindo à API Rest com FastAPI'
    }


@app.get('/datetime')
def get_datetime():
    current_datetime = datetime.now()

    return {
        'datetime': current_datetime
    }


@app.get('/currency_converter/{amount}/{from_currency}/{to_currency}')
def currency_converter(amount: float, from_currency: str, to_currency: str):
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'

    response = requests.get(url)
    data = response.json()
    exchange_rate = data['rates'][to_currency]
    converted_amount = amount * exchange_rate

    return {
        'converted_amount': converted_amount,
        'from_currency': from_currency,
        'to_currency': to_currency
    }


@app.get('/weather/{city}')
def get_weather(city: str):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEYS["openwhether"]}'
    response = requests.get(url)
    data = response.json()
    weather_description = data['weather'][0]['description']
    temperature_kelvin = data['main']['temp']
    temperature_celsius = temperature_kelvin - 273.15

    return {
        'city': city,
        'weather': weather_description,
        'temperature_celsius': temperature_celsius
    }


import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
