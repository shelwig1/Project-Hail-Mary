import numpy as np
from pprint import pprint

#take audio in

#log each note
def get_piano_notes():   
    # White keys are in Uppercase and black keys (sharps) are in lowercase
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
    base_freq = 440 #Frequency of Note A4
    keys = np.array([x+str(y) for y in range(0,9) for x in octave])
    # Trim to standard 88 keys
    start = np.where(keys == 'A0')[0][0]
    end = np.where(keys == 'C8')[0][0]
    keys = keys[start:end+1]
    
    note_freqs = dict(zip(keys, [2**((n+1-49)/12)*base_freq for n in range(len(keys))]))
    note_freqs[''] = 0.0 # stop

    return note_freqs


def matchfreq(inputfreq):
	return inv_map[inputfreq]

x = get_piano_notes()
inv_map = {v: k for k, v in x.items()}
pprint(inv_map)
#take audio
#identify notes in the waveform
#turn those notes into frequencies
#feed those frequencies into our dictionary dictionary