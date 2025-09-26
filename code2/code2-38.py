try:
    numbers = [1, 2, 3]
    print(numbers[3])
except IndexError as e:
    print(f"예외 발생: {e}")
