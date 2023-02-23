import requests
import json
from vanilla_config import base_url

url = "%s/request_favorite_snack" % base_url

payload={}
headers = {}

def favorite_snack():
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text
    data = json.loads(data) # json 파일로 데이터 받아오기

    fav_snack = data["result"]
    snack_label = {
        "chicken_legs": "닭다리",
        "kancho": "칸쵸",
        "rollpoly": "롤리폴리",
        "ramen_snack": "쫄병스낵",
        "whale_food": "고래밥"
    }
    fav_snack_ko = []
    for label in fav_snack:
        fav_snack_ko.append(snack_label[label])
        # print(fav_snack_ko)
    answer_text = '현재 인기 간식은 {} 입니다.'.format(fav_snack_ko)
    return answer_text

if __name__ == "__main__":
    print(favorite_snack())