import requests
import json
from vanilla_config import base_url

# this is test
url = "%s/request_snack_list" % base_url

def snack_list(ko_name):
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text
    data = json.loads(data) # json 파일로 데이터 받아오기

    snack_label = {
        "chicken_legs": "닭다리",
        "kancho": "칸쵸",
        "rollpoly": "롤리폴리",
        "ramen_snack": "쫄병스낵",
        "whale_food": "고래밥"
    }
    ko_names = list(snack_label.values())
    index = ko_names.index(ko_name)
    en_name = list(snack_label.keys())[index]

    result = data["result"]
    for item in result:
        item_name = item["name"]
        if item_name == en_name:
            count = item["count"]
            answer_text = '{} 재고는 {}개 입니다.'.format(ko_name, count)
            break
        else:
            answer_text = '다시 한 번 말씀해주시겠어요?'
    return answer_text

if __name__ == "__main__":
    input_text = '칸쵸'
    print(snack_list(input_text))