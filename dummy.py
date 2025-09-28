import pandas as pd

data_different = {"A": [1, 2, 3], "B": [4, 5], "C": [6]}

# 방법 1: pd.DataFrame(data)
try:
    df1 = pd.DataFrame(data_different)
    print("df1 성공:")
    print(df1)
except Exception as e:
    print(f"df1 에러: {e}")

# 방법 2: pd.DataFrame([data])
try:
    df2 = pd.DataFrame([data_different])
    print("df2 성공:")
    print(df2)
except Exception as e:
    print(f"df2 에러: {e}")


data_list = [
    {"이름": "홍길동", "나이": 25, "거주지": "서울"},
    {"이름": "김철수", "나이": 30, "거주지": "부산"},
    {"이름": "이영희", "나이": 28, "거주지": "대구"}
]

df3 = pd.DataFrame(data_list)
print("df3 = pd.DataFrame(data_list):")
print(df3)
print(f"Shape: {df3.shape}")