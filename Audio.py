import pyaudio
import sys
import wave
import numpy as np
from matplotlib import pyplot as plt
from struct import pack

def sound_to_data(outputFile):
    
    print("hello")

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100 
    DURATION = 5
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT, 
                    channles = CHANNELS,
                    rate = RATE,
                    input = True, 
                    frames_per_buffer = CHUNK)
    
    frames = []
    
    for i in range(0, int(RATE / CHUNK * DURATION)):
        data = stream.read(CHUNK)
        frames.append(data)
        
        

    #stream = p.open()
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(outputFile, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def play(recordedFile):
    CHUNK = 1024
    
    p = pyaudio.PyAudio()
    
    wf = wave.open(recordedFile, 'rb')
    stream = p.open(format = p.get_format_from_width(),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True)
    
    data = wf.readframes(CHUNK)
    
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
     
if(sys.argv[0] == "-r"):
    sound_to_data(sys.argv[1])
else:
    play(sys.argv[1])

