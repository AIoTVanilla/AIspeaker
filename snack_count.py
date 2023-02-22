import requests
import json

url = "http://192.168.50.151:9999/request_snack_count"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

data = response.text
data = json.loads(data) # json 파일로 데이터 받아오기

count = data["result"]

def snack_count(count):
    if count > 5:
        answer_text = '현재 간식 재고 상태는 여유입니다.'
    else:
        answer_text = '현재 간식 재고 상태는 부족입니다.'

    return answer_text
#
# print(snack_count(count))