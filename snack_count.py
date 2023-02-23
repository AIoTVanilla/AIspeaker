import requests
import json
from vanilla_config import base_url

url = "%s/request_snack_count" % base_url

payload={}
headers = {}

def snack_count():
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text
    data = json.loads(data) # json 파일로 데이터 받아오기

    count = data["result"]
    if count > 5:
        answer_text = '현재 간식 재고 상태는 여유입니다.'
    else:
        answer_text = '현재 간식 재고 상태는 부족입니다.'

    return answer_text

if __name__ == "__main__":
    print(snack_count())