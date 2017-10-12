import requests

url = 'http://www.nbrb.by/API/ExRates/Rates/Dynamics/145?startDate=2017-1-1&endDate=2017-10-10'

r = requests.get(url)
print("status code:", r.status_code)

response_dict = r.json()
print(response_dict)
