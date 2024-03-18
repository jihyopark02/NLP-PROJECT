import pyaudio
import sys
import wave
import numpy as np
from matplotlib import pyplot as plt
from struct import pack


def sound_to_data(outputFile):

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100 
    DURATION = 5
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT, 
                    channels = CHANNELS,
                    rate = RATE,
                    input = True, 
                    frames_per_buffer = CHUNK)
    
    print("RECORDING\n")

    frames = []
    
    for i in range(0, int(RATE / CHUNK * DURATION)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    print("STOP\n")

    #stream = p.open()
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(outputFile, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


sound_to_data('output1.wav')


