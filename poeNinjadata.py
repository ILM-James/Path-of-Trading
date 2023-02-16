import requests




findCurrency = ['Mirror of Kalandra', 'Mirror Shard', 'Fracturing Orb', 'Tempering Orb', 'Secondary Regrading Lens', 'Orb of Dominance', 'Tainted Divine Teardrop', 'Orb of Alteration']

def getChaosConversion(findCurrency):
	print(findCurrency)
	response = requests.get('https://poe.ninja/api/data/currencyoverview?league=Sanctum&type=Currency')
	print (response.status_code)
	json_data = response.json() if response and response.status_code == 200 else None
	for orb in findCurrency:
		print(orb)
		if json_data and 'lines' in json_data:
			for currency in json_data['lines']:
		   		if currency['currencyTypeName'] == orb:
		   			value = currency['receive']['value']
		   			if value < 1:
		   				value = int(1 / value)
		   				print(value, orb+'s', 'per Chaos Orb\n')
		   			else:
		   				print('1', orb, 'is', int(value), 'Chaos Orbs\n')

getChaosConversion(findCurrency)