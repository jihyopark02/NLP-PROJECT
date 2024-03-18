import pyaudio
import sys
import wave
import numpy as np
from matplotlib import pyplot as plt
from struct import pack



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
    
