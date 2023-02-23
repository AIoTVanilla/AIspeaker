import requests
import json

url = "http://192.168.50.151:9999/request_snack_list"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

data = response.text
data = json.loads(data) # json 파일로 데이터 받아오기

snacklist = data["result"]
print(snacklist)

snack_label = {
    "chicken_legs": "닭다리",
    "kancho": "칸쵸",
    "rollpoly": "롤리폴리",
    "ramen_snack": "쫄병스낵",
    "whale_food": "고래밥"
}

for key, value in snack_label.items():
    name_en = key
    name_ko = value
    # print(name_en, name_ko)

for index in snacklist:
    list_name = index["name"]
    list_count = index["count"]
    # print(list_name, list_count)
#     for index in snacklist:
#         name = index["name"]
#         count = index["count"]
#         if name_en == name:
#             name = name_ko

def snack_list(name):
    answer_text = ''
    if name in input_text:
        if name_ko == name:
            print(name)
            a = list_name[name_en]
            print(a)
            answer_text = '{} 재고는 {}개 입니다.'.format(name, list_count)
    else:
        answer_text = '다시 한 번 말씀해주시겠어요?'
    return answer_text
#
input_text = '칸쵸'
print(snack_list(input_text))