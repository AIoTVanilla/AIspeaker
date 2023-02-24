from gtts import gTTS
from playsound import playsound
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
import os


is_speak = False

############################################
#                   TTS                    #
############################################    SPEAK
def speaker_tts(text):
    global is_speak
    if is_speak: return
    is_speak = True
    print('[바닐라]' + text)
    tts = gTTS(text=text, lang="ko", tld="co.kr", slow="False")
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    speed = 1.25
    say = AudioSegment.from_file(fp, format="mp3")
    song_speed = say.speedup(playback_speed=speed, chunk_size=150, crossfade=25)
    play(song_speed)
    # if os.path.exists(file_name):   # voice.mp3 파일 삭제
    #     os.remove(file_name)
    is_speak = False

def speak_effect():
    global is_speak
    if is_speak: return
    is_speak = True
    # speed = 1.25
    say = AudioSegment.from_file('resources/dong.wav', format="wav")
    # song_speed = say.speedup(playback_speed=speed, chunk_size=150, crossfade=25)
    play(say)
    # if os.path.exists(file_name):   # voice.mp3 파일 삭제
    #     os.remove(file_name)
    is_speak = False