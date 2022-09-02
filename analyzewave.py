import numpy as np
#import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.fft import fft
from pprint import pprint
"""
TODO:
-dictionary of "words"
-audio input - this may actually be too slow to do it dynamically - create a recording, analyze, spit it out

"""
def analyze(w):
    x = fourier(w)
    x = findfreqs(w)
    print(x)

def fourier(w):
    fftwave = fft(w)
    fftwave = fftwave[:(len(w) // 2)]
    return fftwave

def findfreqs(w):
    peaks, properties = find_peaks(w,100)
    return peaks

