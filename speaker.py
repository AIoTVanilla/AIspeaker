import time, os
import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

# 음성 인식(stt)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[나]' + text)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패')  # 음성 인식 실패한 경우
    except sr.RequestError as e:
        print('요청 실패: {0}'.format(e))  # API key 오류, 네트워크 단절 등

# 대답 출력(txt)
def answer(input_text):
    answer_text =''
    if '바닐라' in input_text:
        answer_text = '네?'
    elif '종료' in input_text:
        answer_text = '종료합니다.'
        stop_listening(wait_for_stop=False)
    else:
        answer_text = '다시 한 번 말씀해주시겠어요?'
    speak(answer_text)

# 대답 출력(audio)
def speak(text):
    print('[바닐라]' + text)
    tts = gTTS(text=text, lang="ko", tld="co.kr", slow="False")
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    speed = 1.25
    say = AudioSegment.from_file(fp, format="mp3")
    song_speed = say.speedup(playback_speed=speed, chunk_size=150, crossfade=25)
    play(song_speed)


r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(m, listen, 4)
# stop_listening(wait_for_stop=False) # 더 이상 듣지 않음

while True:
    time.sleep(0.1)
