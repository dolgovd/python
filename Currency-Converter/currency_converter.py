# Data is sourced from https://free.currencyconverterapi.com

from requests import get
from pprint import PrettyPrinter

# Information from API owner - use free.currconv.com instead of free.currencyconverterapi.com
BASE_URL = 'https://free.currconv.com/'
API_KEY = 'feeaaccca5318e37f535'

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']

    data = list(data.items())
    data.sort()

    return data

def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get('currencySymbol', 'No symbol') # try to find a symbol. Will return 'No symbol' if symbol is not available
        print(f"{_id} - {name} - {symbol}")

def exchange_rate(currency_from, currency_to):
    endpoint = f"api/v7/convert?q={currency_from}_{currency_to}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    response = get(url)

    data = response.json()

    if len(data) == 0:
        print('Invalid currencies')
        return
    rate = list(data.values())[0]
    print(f"{currency_from} --> {currency_to} = {rate}")

    return rate

def convert(currency_from, currency_to, amount):
    rate = exchange_rate(currency_from, currency_to)
    if rate is None:
        return

    try:
        amount =float(amount)
    except:
        print('Invalid amount')
        return

    converted_amount = rate * amount
    print(f"{amount} {currency_from} = {converted_amount} {currency_to}")
    return converted_amount

def main():
    currencies = get_currencies()

    print('Welcome to the currency converter')
    print('Enter "List" to show all available currencies')
    print('Enter "Convert" to convert from one current to another')
    print('Enter "Rate" to get the exchange rate of two currencies/n')
    print()

    while True:
        command = input("Enter a command or q to quit: ").lower()
        if command == 'q':
            break
        elif command == 'list':
            print_currencies(get_currencies())
        elif command == 'convert':
            currency_from = input('Enter a base currency: ').upper()
            amount = input(f'Enter an amount in {currency_from}: ')
            currency_to = input('Enter a currency to convert to: ').upper()
            convert(currency_from, currency_to, amount)
        elif command == 'rate':
            currency_from = input('Enter a base currency: ').upper()
            currency_to = input('Enter a currency to convert to: ').upper()
            exchange_rate(currency_from, currency_to)
        else:
            print('Unrecognized command')
            continue

main()




