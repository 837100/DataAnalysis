temperature_celsius = [25.6, 27.8, 30.5, 22.3, 28.9, 31.2, 24, 7]
celsius_to_fahrenheit = lambda c: (c * 9 / 5) + 32

# 실제로는 이런 과정이 일어납니다:
# map()이 temperature_celsius의 각 요소를 하나씩 celsius_to_fahrenheit 함수에 전달

# 1번째: celsius_to_fahrenheit(25.6) → c=25.6 → (25.6 * 9 / 5) + 32 = 78.08
# 2번째: celsius_to_fahrenheit(27.8) → c=27.8 → (27.8 * 9 / 5) + 32 = 82.04
# 3번째: celsius_to_fahrenheit(30.5) → c=30.5 → (30.5 * 9 / 5) + 32 = 86.9
# ... 이런 식으로 모든 요소에 대해 반복
temperature_fahrenheit = list(map(celsius_to_fahrenheit, temperature_celsius))

print("섭씨 온도 데이터:", temperature_celsius)
print("화씨 온도로 변환:", temperature_fahrenheit)
