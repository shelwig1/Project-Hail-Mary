import make_wave as m
import analyzewave as a
import dictionary

#Simulating recording waves
a_wave = m.get_wave(440)
b_wave = m.get_wave(600)
c_wave = m.combine_wave(m.get_wave(800),m.get_wave(1200))

#Analyze a wave
a_chords = a.analyze(a_wave)
print(a_chords)