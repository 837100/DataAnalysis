import urllib.request
with urllib.request.urlopen('')
as response:
    data = response.read().decode('utf-8')
print(data)