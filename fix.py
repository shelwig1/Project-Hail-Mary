import numpy as np
from scipy.signal import find_peaks
from scipy.fft import fft
from pprint import pprint
import matplotlib.pyplot as plt


samplerate = 44100 #Frequecy in Hz

def combine_wave(w1, w2):
    return np.add(w1,w2)


def get_wave(freq, duration=0.5):
    '''
    Function takes the "frequecy" and "time_duration" for a wave 
    as the input and returns a "numpy array" of values at all points 
    in time
    '''
    
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    
    return wave

def fourier(w):
    fftwave = fft(w)
    fftwave = fftwave[:(len(w) // 2)]
    return fftwave

def findfreqs(w):
    peaks, properties = find_peaks(w,100)
    #double each value of peaks
    return [x*2 for x in peaks]


a = get_wave(440)
b = get_wave(600)
c = combine_wave(a,b)
x = fourier(c)
print(findfreqs(x))
#plt.plot(x)
#plt.show()