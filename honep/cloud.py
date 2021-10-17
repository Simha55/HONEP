import os
from google.cloud import speech
mp3 = 'demo.mp3'
wav = 'demo.wav'
os.environ['cred'] = 'client_service_key.json'
sc = speech.SpeechClient()




with open(mp3, 'rb') as f1:
    byte_mp3 = f1.read()
aud_mp3 = speech.RecognitionAudio(content=byte_mp3)

with open(wav, 'rb') as f2:
    byte_wav = f2.read()
aud_wav = speech.RecognitionAudio(content=byte_wav)

config1 = speech.RecognitionConfig(
    sample_rate_hertz=48000,
    enable_automatic_punctuation=True,
    language_code='en-US'
)

config2 = speech.RecognitionConfig(
    sample_rate_hertz=44100,
    enable_automatic_punctuation=True,
    language_code='en-US',
    audio_channel_count=2
)



response_standard_wav = speech_client.recognize(
    config=config2,
    audio=aud_wav
)
response_standard_mp3 = speech_client.recognize(
    config=config1,
    audio=aud_mp3
)

print(response_wav)
print(response_mp3)

uri = 'c://vid.wav'
long__wav = speech.RecognitionAudio(uri=uri)

config_wav_enhanced = speech.RecognitionConfig(
    sample_rate_hertz=48000,
    enable_automatic_punctuation=True,
    language_code='en-US',
    use_enhanced=True,
    model='video'
)

operation = speech_client.long_running_recognize(
    config=config_wav,
    audio=long_wav
)
response = operation.result(timeout=90)
print(response)

for result in response.results:
    print(result.alternatives[0].transcript)
    print(result.alternatives[0].confidence)
    print()