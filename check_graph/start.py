import requests
from datetime import datetime
import currency_graph as cg

def read_year():
    year = input('Input year (default - current year) ')
    try:
        year = int(year)
    except ValueError:
        year = datetime.today().year
    return year

def read_currencies():
    currencies = []
    while True:
        currency = input('Input curency abbreviation ')
        if currency:
            currencies.append(currency.upper())
        else:
            break
    return currencies

def read_filename():
    filename = input('Input filename to save (not requared) ')
    if filename and not filename.endswith('.svg'):
        filename += '.svg'
    return filename

def main():
    year = read_year()
    currencies = read_currencies()
    filename = read_filename()

    cg.create_currency_graph(currencies, year, filename)

main()
