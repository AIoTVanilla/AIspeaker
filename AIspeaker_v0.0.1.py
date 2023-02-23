import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
# import snack_tracking as st
import favorite_snack as fs
import snack_count as sc
import snack_list as sl
import socketio
############################################
#                   STT                    #
############################################    LISTEN
def speaker_stt(r, audio):
    try:
        # 구글 API로 인식 (하루 50회)
        text = r.recognize_google(audio, language='ko')
        print('[나]' + text)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패') # 음성 인식 실패한 경우
    except sr.RequestError as e:
        print('요청 실패: {0}'.format(e))   # API key 오류, 네트워크 단절 등

############################################
#                   TTS                    #
############################################    SPEAK
def speaker_tts(text):
    print('[바닐라]' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):   # voice.mp3 파일 삭제
        os.remove(file_name)

############################################
#                   ANS                    #
############################################

snack_label = {
    "chicken_legs": "닭다리",
    "kancho": "칸쵸",
    "rollpoly": "롤리폴리",
    "ramen_snack": "쫄병스낵",
    "whale_food": "고래밥"
}

def answer(input_text):
    answer_text =''
    if '바닐라' in input_text: # wake-up word
        answer_text = '무엇을 도와드릴까요?'
    elif '종료' in input_text:
        answer_text = '종료합니다.'
        stop_listening(wait_for_stop=False)
    elif '인기' in input_text:    # favorite_snack
        answer_text = '현재 인기 간식은 {} 입니다.'.format(fs.favorite_snack())
    elif '재고' in input_text:    # snack_count
        answer_text = sc.snack_count()
    elif name in input_text:    # snack_list
        answer_text = sl.snack_list(name)
    else:
        answer_text = '다시 한 번 말씀해주시겠어요?'
    speaker_tts(answer_text)

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
        answer_text = '간식이 들어왔습니다.'
    else:
        answer_text = '간식 재고가 없습니다.'
    return answer_text

@sio.on('response')
def response(data):
    print('response', data)
###########################################
r = sr.Recognizer()
m = sr.Microphone()

stop_listening = r.listen_in_background(m, speaker_tts)
# stop_listening(wait_for_stop=False) # 더 이상 듣지 않음

while True:
    time.sleep(0.1)
