import urllib.request

x = urllib.request.urlopen('https://www.cars.co.za/')

print(x.read())
