import requests
import json

url = "https://api.open-meteo.com/v1/forecast?=&=&current=temperature_2m"
params = {
    "latitude": "37.58638333",
    "longitude": "127.0203333",
    "current": "temperature_2m",
}

try:
    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()

    data = response.json()
    print("API 응답: ", data)
    print(
        "서울시의 종로구의 현재 온도는 : {0}{1} 입니다.".format(
            data["current"]["temperature_2m"], data["current_units"]["temperature_2m"]
        )
    )

except requests.exceptions.RequestException as e:
    print(f"API 호출 실패: {e}")
except json.JSONDecodeError as e:
    print(f"JSON 파싱 실패: {e}")
