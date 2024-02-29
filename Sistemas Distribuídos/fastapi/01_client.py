#!/usr/bin/python3
'''API REST client.'''
import requests

# URL base da API
BASE_URL = "http://127.0.0.1:8000"  # Altere para o endereço onde sua API está sendo executada


def get_root():
    url = f"{BASE_URL}/"
    response = requests.get(url)
    return response.json()


def get_datetime():
    url = f"{BASE_URL}/datetime"
    response = requests.get(url)
    return response.json()


def currency_converter(amount, from_currency, to_currency):
    url = f"{BASE_URL}/currency_converter/{amount}/{from_currency}/{to_currency}"
    response = requests.get(url)
    return response.json()


def get_weather(city):
    url = f"{BASE_URL}/weather/{city}"
    response = requests.get(url)
    return response.json()


def main(*_args) -> None:
    print("Mensagem da raiz:")
    print(get_root())
    print("\nData e hora atual:")
    print(get_datetime())
    print("\nConversão de moeda:")
    print(currency_converter(100, "USD", "EUR"))
    #print("\nPrevisão do tempo:")
    #print(get_weather("London"))


if __name__ == "__main__":
    main()
