import json
import pandas as pd

data = [
    {
        "이름": "홍길동",
        "나이": 25,
        "거주지": "서울",
        "관심사": ["프로그래밍", "데이터 분석"],
    },
    {
        "이름": "김철수",
        "나이": 30,
        "거주지": "부산",
        "관심사": ["요리", "여행", "독서"],
    },
    {"이름": "이영희", "나이": 28, "거주지": "대구", "관심사": ["운동"]},
]

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

df = pd.DataFrame([data])
df.to_json("output_df.json", orient="records", indent=4, force_ascii=False)
