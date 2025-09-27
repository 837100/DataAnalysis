import json
import pandas as pd

with open('data.json', 'r', encoding = 'utf-8') as f:
    data = json.load(f)
print(data)
df = pd.read_json('data.json', orient = 'records', encoding = 'utf-8', lines = False)
print(df)