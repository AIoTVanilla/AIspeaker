import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
############################################
#                   STT                    #
############################################
r = sr.Recognizer()
m = sr.Microphone()

def speaker_stt(r, m, source):
    with m as source:
        print('듣고 있어요.')
        audio = r.listen(source)    # 마이크로부터 음성 듣기

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

