osda_students = [
    {"name": "김지원", "score": 85},
    {"name": "이민준", "score": 65},
    {"name": "박서연", "score": 90},
    {"name": "정현우", "score": 55},
    {"name": "최예은", "score": 78},
]

passed_students = list(filter(lambda student: student["score"] >= 70, osda_students))
print("70점 이상 합격한 학생 목록:")
for student in passed_students:
    print(f"이름: {student['name']}, 점수 {student['score']}")
