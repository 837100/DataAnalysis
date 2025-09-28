import pandas as pd
import json

data = {
    "이름": ["김철수", "이영희", "박민수", "최치훈", "정소희"],
    "학년": [1, 2, 3, 4, 2],
    "학점": [4.2, 3.8, 4.5, 3.9, 3.5],
    "학과": ["컴퓨터학", "경영학", "농학", "교육학", "영어영문학"],
    "동아리": ["축구", "농구", "야구", "배구", "탁구"],
}

df1 = pd.DataFrame.from_dict(data)
df2 = pd.read_csv("students.csv", encoding="utf-8")
df3 = pd.read_json("students.json")

print(df1)
print(df2)
print(df3)