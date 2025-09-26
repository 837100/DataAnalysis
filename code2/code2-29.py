def get_dataset_status(values):
    return min(values), max(values), sum(values) / len(values)

data = [12, 8, 21, 17, 5, 32, 14]
minimun, maxium, average = get_dataset_status(data)
print(f'최솟값: {minimun}, 최댓값: {maxium}, 평균: {average:.2f}')

