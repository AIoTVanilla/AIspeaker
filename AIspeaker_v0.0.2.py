import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import socketio
import requests
import json
############################################
#                   STT                    #
############################################
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[나]' + text)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패')  # 음성 인식 실패한 경우
    except sr.RequestError as e:
        print('요청 실패: {0}'.format(e))  # API key 오류, 네트워크 단절 등

############################################
#                   TTS                    #
############################################
def speak(text):
    print('[바닐라]' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists("./file_name"):   # voice.mp3 파일 삭제
        os.remove(file_name)

############################################
#                   ANS                    #
############################################
def answer(input_text):
    answer_text =''
    if '바닐라' in input_text:
        answer_text = '무엇을 도와드릴까요?'
    elif '인기' in input_text:
        answer_text = favorite_snack()
    elif '현재 재고' in input_text:
        answer_text = snack_count()
    elif a in input_text:
        answer_text = snack_list()
    elif '종료' in input_text:
        answer_text = '종료합니다.'
        stop_listening(wait_for_stop=False)
    else:
        answer_text = '다시 한 번 말씀해주시겠어요?'
    speak(answer_text)

############################################
#              SNACK_TRACKING              #
############################################
sio = socketio.Client()
sio.connect('ws://192.168.50.151:9999')

@sio.on('snack')
def snack(data):
    # print('snack', data, type(data))
    result = data.get('result')
    # print(result)
    if result == True:
        speak('간식이 들어왔습니다.')
    else:
        speak('간식 재고가 없습니다.')

@sio.on('response')
def response(data):
    print('response', data)

############################################
#                FAV_SNACK                 #
############################################
url = "http://192.168.50.151:9999/request_favorite_snack"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

data = response.text
data = json.loads(data) # json 파일로 데이터 받아오기

fav_snack = data["result"]
# print(fav_snack)

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
        # print(fav_snack_ko)
    answer_text = '현재 인기 간식은 {} 입니다.'.format(fav_snack_ko)
    return answer_text

############################################
#                SNACK_CNT                 #
############################################
url1 = "http://192.168.50.151:9999/request_snack_count"

payload={}
headers = {}

response1 = requests.request("GET", url1, headers=headers, data=payload)

# print(response.text)

data1 = response1.text
data1 = json.loads(data1) # json 파일로 데이터 받아오기

count = data1["result"]

def snack_count(count):
    if count > 5:
        answer_text = '현재 간식 재고 상태는 여유입니다.'
    else:
        answer_text = '현재 간식 재고 상태는 부족입니다.'

    return answer_text

############################################
#                SNACK_LST                 #
############################################

url2 = "http://192.168.50.151:9999/request_snack_list"

payload={}
headers = {}

response2 = requests.request("GET", url2, headers=headers, data=payload)

# print(response.text)

data2 = response2.text
data2 = json.loads(data2) # json 파일로 데이터 받아오기

snacklist = data2["result"]
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
        answer_text = '{} 재고는 {}개 입니다.'.format(name, count)
    else:
        answer_text = '다시 한 번 말씀해주시겠어요?'
    return answer_text

###########################################
r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(m, listen)
# stop_listening(wait_for_stop=False) # 더 이상 듣지 않음

while True:
    time.sleep(0.1)
