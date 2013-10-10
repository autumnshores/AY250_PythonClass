#Find the notes in a given file

import aifc
%pylab
import matplotlib.pyplot as plt
import numpy as np
from scipy import *

def FindNotes(filename):
    #load and read .aif file
    #filename = "sound_files/2.aif"
    a = aifc.open(filename, 'rb')
    data = a.readframes(a.getnframes())
    RATE = a.getframerate()
    #get integer form of audio file and time for amplitude vs. time plot
    integer_data = np.fromstring(data, dtype=np.int32).byteswap()
    time = arange(size(integer_data)) / float(RATE)
    
    #do FFT and get frequency spectrum
    n = size(integer_data)
    k = arange(n)
    T = n/float(RATE)
    freq = k/T
    freq = freq[range(n/2)] #one side of the frequency range
    
    spectrum = rfft(integer_data)/n #normalizing
    spectrum = spectrum[range(n/2)]
    
    #now plot Amplitude vs. time
    plot_title = ("Waveform")
    fig = plt.figure(figsize=(7, 4.5))
    ax1 = fig.add_subplot(1,1,1)
    ax1.plot(time, integer_data, color="red", linestyle="-")
    ax1.set_xlabel("Time [s]")
    ax1.set_ylabel("Amplitude")
    ax1.set_xlim(min(time), max(time))
    ax1.set_title(plot_title)
    show()
    
    #and plot Frequency spectrum
    plot2_title = ("Frequency spectrum")
    fig2 = plt.figure(figsize=(7, 4.5))
    ax2 = fig2.add_subplot(1,1,1)
    ax2.plot(freq, abs(spectrum), color="blue", linestyle="-")
    ax2.set_xlabel("Frequency [Hz]")
    ax2.set_ylabel("Power [dB]")
    ax2.set_xlim(0, 2000)
    ax2.set_title(plot2_title)
    show()
    
    #find number of peaks above a certain threshold (set here to be 0.3 of the max peak power)
    threshold = 0.3*max(abs(spectrum))
    mask = abs(spectrum) > threshold
    peaks = freq[mask]
    x = np.diff(peaks)
    y = np.where(abs(x)>10)
    print "There are", size(y[0])+1, "major peaks in the spectrum that are above 0.3 of the max. peak power"
    
    sortpeaks = argsort(abs(spectrum))[::-1][:n]
    peak_frequency = freq[sortpeaks[0]]
    print "The peak frequency is", peak_frequency, "Hz"
    
    #calculate top peak frequencies
    sortpeaks = argsort(abs(spectrum))[::-1][:n]
    peak_frequency = freq[sortpeaks[0]]
    
    freqs = []
    for i in range(len(sortpeaks)):
        freqs.append(freq[sortpeaks[i]])
    
    a = np.diff(freqs)
    b = np.where(abs(a)>10)
    
    frequencies = []
    frequencies.append(peak_frequency)
    for j in range(len(b[0])):
        frequencies.append(freqs[b[0][j]+1])
    
    
    x = sort(frequencies[0:10])
    y = np.diff(x)
    z = np.where(abs(y)>5)
    majfreq = []
    for k in range(len(z[0])):
        majfreq.append(x[z[0][k]])
    
    
    print "The major peak frequencies detected are around", majfreq, "Hz"
    return majfreq
