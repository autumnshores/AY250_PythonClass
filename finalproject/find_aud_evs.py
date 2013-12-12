# find_aud_evs.py

"""
This script will mark the start(onset) and end (offset) times (in samples) of all 
the auditory events in the spkr analog file. Input arguments are:

- analog speaker data (spkr)
- threshold number (thresh)
- contiguous noise block large enough to define point of stimulus end (noise_block)
- maximum stimulus length (max_length)

Returns: an array of onset and offset times

"""
import numpy as np

def find_aud_evs(spkr,thresh,noise_block,max_length):

    start = 0                  # temporary start stimulus point
    finish = 0                 # temporaty finish stimulus point
    cnt_noise = 0              # counter for noise block
    i = 0                      # counter for stimulus number
    st = 0                     # counter for position within the signal
    auds = []
    
    while st < len(spkr):
        if spkr[st]>thresh or spkr[st]<(-thresh):   # above noise
            if start == 0:                          # haven't reached stimulus start yet
                start  = st
            else:
                finish = st
            cnt_noise = 0
        elif start != 0:                          # in noise and haven't saved last stimulus
            cnt_noise = cnt_noise+1
            if cnt_noise > noise_block:              # contiguous noise block -> save last stimulus
                if (st-start) > max_length:        # skip detected stim because it is larger than max_length
                    start = 0
                    finish = 0
                else:
                    auds.append([start,finish])
                    i = i+1
                    start = 0
                    finish = 0
        st = st+1
    return auds