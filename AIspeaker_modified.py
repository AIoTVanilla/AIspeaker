import time, os
import favorite_snack as fs
import snack_count as sc
import snack_list as sl
import snack_tracking
from sound_utils import speaker_tts
import speech_recognition as sr

snack_label = {
    "chicken_legs": "닭다리",
    "kancho": "칸쵸",
    "rollpoly": "롤리폴리",
    "ramen_snack": "쫄병스낵",
    "whale_food": "고래밥"
}


############################################
#                   STT                    #
############################################    LISTEN
def speaker_stt(r, audio):
    try:
        # 구글 API로 인식 (하루 50회)
        text = r.recognize_google(audio, language='ko', show_all=True)
        if 'alternative' in dict(text).keys():
            text = dict(text)['alternative'][0]['transcript']
        else:
            text = ""
        print(text)
        # print('[나]' + text)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패') # 음성 인식 실패한 경우
    except sr.RequestError as e:
        print('요청 실패: {0}'.format(e))   # API key 오류, 네트워크 단절 등
    except Exception as err:
        print('[Error]', err)


############################################
#                   ANS                    #
############################################

def answer(input_text):
    try:
        answer_text =''
        if '바닐라' in input_text: # wake-up word
            answer_text = '무엇을 도와드릴까요?'
        elif '종료' in input_text:
            answer_text = '종료합니다.'
            stop_listening(wait_for_stop=False)
        elif '인기' in input_text:    # favorite_snack
            answer_text = fs.favorite_snack()
        elif '재고' in input_text:    # snack_count
            answer_text = sc.snack_count()
        elif input_text in snack_label.values():    # snack_list
            answer_text = sl.snack_list(input_text)
        else:
            answer_text = '다시 한 번 말씀해주시겠어요?'
        speaker_tts(answer_text)
    except Exception as ex:
        print("[Error]", ex)


if __name__ == "__main__":
    ###########################################
    r = sr.Recognizer()
    m = sr.Microphone()

    ############################################
    #              SNACK_TRACKING              #
    ############################################

    stop_listening = r.listen_in_background(m, speaker_stt, 4)
    # stop_listening(wait_for_stop=False) # 더 이상 듣지 않음

    while True:
        time.sleep(0.1)
