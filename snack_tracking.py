import socketio

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

