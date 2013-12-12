# create_spect.py

"""
This script will generate spectrograms for the electrode channel specified. Input
arguments required are:

- electrode data (gdatInput)
- sampling rate (srate)
- maximum frequency for spectrogram generation (maxfreq)
- compression factor (compress)

The input data (gdatInput) will first be trimmed to make its length an exact 
multiple of the compression factor (compress). FFT will be applied, and the signal
will be filtered in each frequency band (specified using the create_freqs module)
using a flattened gaussian* filter, before being transformed back (ifft) into the
time domain. These filtered signals are then resampled using scipy.signal.resample 
with the specified compression factor (compress) and normalized. 

*Flattened gaussian: where the maximum point is flattened to length (upper_bound - 
lower_bound)

Returns: an array of frequency filtered spectrograms

"""
import numpy as np
import math
import scipy
from scipy import *
from scipy import signal


""" create_freqs module
In this module, the frequencies will be generated in bands from 1 -
maxfreq Hz, logarithmically spaced (log_spacing) and with a minimum spacing
(min_delta) between frequencies.
"""

def create_freqs(min_f,max_f,min_delta,log_spacing):
    x = np.arange(log10(min_f),log10(max_f),log_spacing)
    freqs = 10**x
    i = 1
    while (i<=len(freqs)-1):
        if ((freqs[i]-freqs[i-1])<min_delta):
            freqs=np.delete(freqs,i)
        else:
            i = i+1
    return freqs

"""my_hilbert module
In this module, the FFTed signal will be filtered in the respective frequency bands
as specified in the create_freqs module using a flattened gaussian filter, and is
transformed back into the time domain.

CURRENTLY BROKEN, NEEDS FIXING
"""

def my_hilbert(gdatinput, sampling_rate, lower_bound, upper_bound):
    max_freq = sampling_rate/2.
    df=2*max_freq/len(gdatinput)
    center_freq=(upper_bound+lower_bound)/2
    filter_width=upper_bound-lower_bound
    x=np.arange(0,max_freq,df)
    gauss_width = 1
    
    gauss=exp(-(x-center_freq)**2*gauss_width)
    cnt_gauss = round(center_freq/df)
    flat_padd = round(filter_width/df)  #flat padding at the max value of the gaussian
    padd_left = floor(flat_padd/2)
    padd_right = ceil(flat_padd/2)
    
    a = np.array(gauss[(padd_left):cnt_gauss])
    b = np.array([1.]*int(flat_padd))
    c = np.array(gauss[(cnt_gauss):(len(gauss)-padd_right)])
    our_wind = np.concatenate((a,b,c))
    print len(our_wind)
    d = np.array([0.]*(len(gdatinput)-len(our_wind)))
    our_wind2 = np.concatenate((our_wind,d))*2

    
    filt_signal=ifft(gdatinput*our_wind2)
    return filt_signal

"""The main spectrogram creation module
This module will transform the input signal gdatInput into the frequency domain,
filter it into the respective frequency bands and transform them back into the time
domain. Analytic power is calculated by taking the modulus squared of the output
signal, and is compressed and normalized.
"""

def create_spect(gdatInput,srate,maxfreq,compress):
    gdatInput=gdatInput[0:(len(gdatInput)-(len(gdatInput)%compress))] #cut the end of the data to make it an exact multiple of compression
    fgdat=fft(gdatInput)
    freqs = create_freqs(1,maxfreq,0.8,0.04)
    num_cntr_f = len(freqs)
    SPEC=zeros((num_cntr_f,int(len(fgdat))/compress)) #initiate  the output spectogram matrix
    MN=zeros((num_cntr_f,1))                     #initiate  the output mean vector
    STD=zeros((num_cntr_f,1))                     #initiate  the output standard deviation vector
    
    # the heart of the spectogram
    for i in range(num_cntr_f):
        f = freqs[i]
        bp_Input=my_hilbert(fgdat,srate,f-0.1*f,f+0.1*f)
        short_bp_Input=abs(bp_Input)**2             #calculate analytic power
        MN[i]=mean(short_bp_Input)                        # calculate the mean of the data in a freq band
        STD[i]=std(short_bp_Input)                        # calculate the std of the data in a freq band
        SPEC[i]=scipy.signal.resample(short_bp_Input, len(short_bp_Input)/compress) #compress the spectogram

    for f in range(len(freqs)):
        SPEC[f] = SPEC[f]/MN[f] #normalize the spectrogram
    return SPEC