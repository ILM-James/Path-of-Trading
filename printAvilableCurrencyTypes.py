import requests

response = requests.get('https://poe.ninja/api/data/currencyoverview?league=Sanctum&type=Currency')
print (response.status_code)
json_data = response.json() if response and response.status_code == 200 else None

if json_data and 'lines' in json_data:
	for currency in json_data['lines']:
		print(currency['currencyTypeName'])