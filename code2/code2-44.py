students = [
    ("김지은", 85),
    ("이민수", 92),
    ("박서현", 78),
    ("정준호", 88),
    ("최유진", 95),
]
sorted_students = sorted(students, key=lambda student: student[1])

print("성적 오름차순 정렬 결과:")
for name, score in sorted_students:
    print(f"{name}: {score}점")
