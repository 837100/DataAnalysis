city_population = {
    '서울': 957, '부산': 339, '인천': 294, '대구': 242, '광주': 145,
    '대전': 147, '울산': 114, '세종':36, '수원':115, '창원': 103,
    '고양': 105, '용인': 108, '성남': 94
}
large_cities = {city: pop for city, pop in city_population.items() if pop >= 200}

print('인구 200만 명 이상의 도시:', large_cities)
large_short_name_cities = {city: pop for city, pop in city_population.items() if pop >= 300 and '산' in city}