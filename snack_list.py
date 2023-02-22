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
# print(snacklist)

for index in snacklist:
    name = index["name"]
    # print(name)
    count = index["count"]
    # print(count)

snack_label = {
    "chicken_legs": "닭다리",
    "kancho": "칸쵸",
    "rollpoly": "롤리폴리",
    "ramen_snack": "쫄병스낵",
    "whale_food": "고래밥"
}
# for value in snack_label.values():
#     name_ko = value
#     print(name_ko)

def snack_list(name):
    answer_text = ''
    if name in input_text:
        answer_text = print('{} 재고는 {}개 입니다.'.format(name, count))
    else:
        print('다시 한 번 말씀해주시겠어요?')
    return answer_text
#
# input_text = '칸쵸'
# snack_list(input_text)