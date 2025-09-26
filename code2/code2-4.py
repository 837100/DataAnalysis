matrix = [
    [1,2,3,4],
    [5,6,7,9],
    [9,10,11,12],
    [13,14,15,16]
]
first_two_rows = matrix[:2]
print(first_two_rows)
first_two_columns = [row[ :2] for row in matrix]
print(first_two_columns)