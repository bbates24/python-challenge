import requests

x = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&appid=9efd0c479c718c66e129d30ac7053e00')

print(x.text)