from gtts import gTTS
from playsound import playsound

is_speak = False

############################################
#                   TTS                    #
############################################    SPEAK
def speaker_tts(text):
    global is_speak
    if is_speak: return
    is_speak = True
    print('[바닐라]' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    # if os.path.exists(file_name):   # voice.mp3 파일 삭제
    #     os.remove(file_name)
    is_speak = False
