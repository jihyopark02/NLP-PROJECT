import pyaudio
import sys
import wave
import numpy as np
import pandas as pd
from glob import glob

import librosa
import librosa.display

import IPython.display as ipd
from itertools import cycle
from matplotlib import pyplot as plt
from struct import pack



data, sr = librosa.load('output1.wav')
print(data)
print(np.shape(data))


