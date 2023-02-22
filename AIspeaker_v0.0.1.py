import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import snack_tracking as st
import favorite_snack as fs
import snack_count as sc
import snack_list as sl
############################################
#                   STT                    #
############################################
r = sr.Recognizer()
m = sr.Microphone()

with m as source:
    print('듣고 있어요.')
    audio = r.listen(source)  # 마이크로부터 음성 듣기

def speaker_stt(r, audio):
    try:
        # 구글 API로 인식 (하루 50회)
        text = r.recognize_google(audio, language='ko')
        print('[나]' + text)
    except sr.UnknownValueError:
        print('인식 실패') # 음성 인식 실패한 경우
    except sr.RequestError as e:
        print('요청 실패: {0}'.format(e))   # API key 오류, 네트워크 단절 등

############################################
#                   TTS                    #
############################################
def speaker_tts(text):
    print('[바닐라]' + text)
    tts_ko = gTTS(text = text, lang = 'ko')
    tts_ko.save(file_name)
    playsound(file_name)    #.mp3 파일 재생

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
    if '바닐라' in input_text:
        answer_text = '무엇을 도와드릴까요?'
    elif '종료' in input_text:
        answer_text = '종료합니다.'
        stop_listening(wait_for_stop=False)
    elif '인기' in input_text:
        answer_text = '현재 인기 간식은 {} 입니다.'.format(fs.favorite_snack())
    elif '재고' in input_text:
        answer_text = sc.snack_count()
    elif name in input_text:
        answer_text = sl.snack_list(name)
    else:
        answer_text = '다시 한 번 말씀해주시겠어요?'
    speaker_tts(answer_text)


