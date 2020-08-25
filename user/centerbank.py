import requests
import re
resp = requests.get('http://cbr.ru')
html = resp.text
match = re.search(r'Евро\D+(\d+,\d+)', html)
match1 = re.search(r'Доллар\D+(\d+,\d+)', html)
rate = match.group(1)
rate2 = match1.group(1)

def dollar():
    return float(rate2.replace(',','.'))

def euro():
    return float(rate.replace(',','.'))
