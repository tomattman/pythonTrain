from datetime import datetime, date
import pygal
from collections import defaultdict
import requests

def create_currency_graph(currencies, year, filename = None):
    currencies_codes = get_valid_currencies(currencies, get_currencies_names())

    create_graph(currencies_codes, year, filename)

def get_valid_currencies(currencies, all_currencies):
    valid_currencies = {}
    for currency in currencies:
        if all_currencies.get(currency, None):
            valid_currencies[currency] = all_currencies.get(currency)
        else:
            print('no valid currency abbreviation {0}'.format(currency))
    if len(valid_currencies) == 0:
        valid_currencies['USD'] = all_currencies.get('USD')
    return valid_currencies

def get_currencies_names():
    r = requests.get('http://www.nbrb.by/API/ExRates/Currencies')
    if r.status_code == 200:
        names_dict = {}
        for currency in r.json():
            names_dict[currency['Cur_Abbreviation']] = currency['Cur_ID']
        return names_dict

def create_graph(currencies_codes, year, filename):
    dateline = pygal.DateLine(x_label_rotation = 90)

    for key in currencies_codes:
        url = 'http://www.nbrb.by/API/ExRates/Rates/Dynamics/{c_code}?startDate={0}-1-1&endDate={0}-12-31'.format(year, c_code = currencies_codes[key])
        response = requests.get(url)
        if response.status_code == 200:
            get_currency_rait_by_year(dateline, key, response.json())
        else:
            print('Cannot read currency rait for {0}'.format(key))
            currencies_codes.pop('key', None)

    if not filename:
        filename = ""
        for key in currencies_codes:
            filename += "{0}-".format(key)
        filename += str(year)
        filename += ".svg"

    dateline.render_to_file(filename)

def get_currency_rait_by_year(dateline, currency_name, response_body):
    dateline.x_labels = get_x_scale_labels(response_body)
    dateline.add(currency_name, get_line_for_graph(response_body))

def get_x_scale_labels(response_body):
    dates = []
    for number, currency in enumerate(response_body):
        currency_date_time = datetime.strptime(currency['Date'],'%Y-%m-%dT%H:%M:%S')
        currency_date = date(currency_date_time.year, currency_date_time.month, currency_date_time.day)
        if number % 7 == 0:
            dates.append(currency_date)

def get_line_for_graph(response_body):
    values = []
    for currency in response_body:
        currency_date_time = datetime.strptime(currency['Date'],'%Y-%m-%dT%H:%M:%S')
        currency_date = date(currency_date_time.year, currency_date_time.month, currency_date_time.day)
        currency_rait = currency['Cur_OfficialRate']
        values.append((currency_date, float(currency_rait)))
    return values



def show_currency_rait_by_month(response_body, file_name = "usd_rait_month.svg"):
    data = defaultdict(lambda: [])
    for currency in response_body:
        currency_date_time = datetime.strptime(currency['Date'],'%Y-%m-%dT%H:%M:%S')
        currency_rait = currency['Cur_OfficialRate']
        data[currency_date_time.strftime("%B")].append(currency_rait)

    line_chart = pygal.Line()
    line_chart.title = "Usd raits by month days"
    line_chart.x_labels = map(str, range(1, 32))
    for key in data:
        line_chart.add(key, data[key])

    line_chart.render_to_file(file_name)
