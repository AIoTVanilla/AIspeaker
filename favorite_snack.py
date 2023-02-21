import requests
import json


url = "http://192.168.50.151:9999/request_favorite_snack"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

data = response.text
data = json.loads(data) # json 파일로 데이터 받아오기

fav_snack = data["result"]
print(fav_snack)

snack_label = {
    "chicken_legs": "닭다리",
    "kancho": "칸쵸",
    "rollpoly": "롤리폴리",
    "ramen_snack": "쫄병스낵",
    "whale_food": "고래밥"
}

def favorite_snack():
    fav_snack_ko = []
    for label in fav_snack:
        fav_snack_ko.append(snack_label[label])
        print(fav_snack_ko)

    return fav_snack_ko
print('현재 인기 간식은 {} 입니다.'.format(favorite_snack()))