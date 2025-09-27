import urllib.request
with urllib.request.urlopen('https://github.com/837100/Data-Analysis-with-Open-Source/blob/main/Chapter%203/students.csv') as response:
    data = response.read().decode('utf-8')
print(data)