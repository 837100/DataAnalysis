scores = {"김철수": 45, "이영희": 38, "박지성": 49, "최민수": 30, "정수정": 42}
percentage_scores_old = { } 
for name, score in scores.items():
    percentage_scores_old[name] = (scores / 50) * 100
print("기존 방식 결과:", percentage_scores_old)
