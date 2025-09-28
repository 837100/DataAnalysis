import pandas as pd

data = {
    "이름": ["김철수", "이영희", "박민수", "최치훈", "정소희"],
    "학년": [1, 2, 3, 4, 2],
    "학점": [4.2, 3.8, 4.5, 3.9, 3.5],
    "학과": ["컴퓨터학", "경영학", "농학", "교육학", "영어영문학"],
    "동아리": ["축구", "농구", "야구", "배구", "탁구"],
}
df = pd.DataFrame(data)

print("index:\n", df.index)
print("\ncolumns:\n", df.columns)
print("\nvalues:\n", df.values.flatten())
print("\nrows:\n", df.values.tolist())
