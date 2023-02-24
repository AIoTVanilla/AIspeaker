#!/usr/bin/env python

def run_quickstart():
    #global str_b
    import io
    import os

    from google.cloud import speech
    from audio import audio_write
    
    client = speech.SpeechClient()

    os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "C:/Users/SBAUser/Downloads/quisvox_200318/client_secret_199144286179-6t0g49h8ec8cqn11jdaqgb06dhs9mhkv.apps.googleusercontent.com.json")
    print(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))

    str_o = audio_write('10')
    str_o = ''
    file_name = os.path.join(
            os.path.dirname(__file__),
            'file.wav')

    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)
    print(type(audio))
    config = types.RecognitionConfig(
            encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code='ko-KR')

    request = speech.RecognizeRequest(request={"config": config, "audio": audio})
    response = client.list_voices(request=request)

    for result in response.results:
        print('Transcrpit: {}'.format(result.alternatives[0].transcript.encode('utf-8')))
        str_s = result.alternatives[0].transcript.encode('utf-8')
        print (str_s)
        return str_s
if __name__ == '__main__':
    run_quickstart()

def check_word(try_cnt):
    import io
    import os

    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    
    if try_cnt == '0':

        client = speech.SpeechClient()
        check_file = os.path.join(
                os.path.dirname(__file__),
                'test.wav')
        print(check_file)

    elif try_cnt == '55':
        client = speech.SpeechClient()
        check_file = os.path.join(
                os.path.dirname(__file__),
                'start.wav')
        print(check_file)
    with io.open(check_file, 'rb') as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
            encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code='ko-KR')

    request = speech.RecognizeRequest(request={"config": config, "audio": audio})
    response = client.list_voices(request=request)


    for result in response.results:
        print('Transcrpit: {}'.format(result.alternatives[0].transcript.encode('utf-8')))
        str_b = result.alternatives[0].transcript.encode('utf-8')
        return str_b
