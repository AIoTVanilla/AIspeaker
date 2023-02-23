import socketio
from vanilla_config import websocket_url
import threading
from sound_utils import speaker_tts

sio = socketio.Client()
def start_websocket():
    sio.connect(websocket_url)
    print("websocket:", websocket_url)

t = threading.Thread(target=start_websocket, args=())
t.setDaemon(True)
t.start()

@sio.on('snack')
def snack(data):
    result = data.get('result')
    if result == True:
        answer_text = '간식이 들어왔습니다.'
    else:
        answer_text = '간식 재고가 없습니다.'
    speaker_tts(answer_text)

@sio.on('response')
def response(data):
    print('response', data)

