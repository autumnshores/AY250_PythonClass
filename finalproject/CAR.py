# CAR.py

"""
This script will calculate the common average reference (CAR) from a set of
electrode channels and return an array of electrode channels with the CAR
subtracted from them. Input arguments required are:

- Total number of electrodes (Enum)
- Number of electrodes per group (grouping) ** this number should ideally be a 
    multiple of Enum, or should satisfy the following condition: 
    Enum%grouping > grouping/2
- List of good electrodes (elecs)
- List of bad electrodes (bad_elecs)

This particular method of CAR subtraction involvesccalculating the CAR in groups and 
subtracting this CAR from electrodes in their respective groups, before subtracting 
the common CAR from each individual electrode. Electrodes marked as bad are excluded 
from the CAR.

"""
import numpy as np
import math
from math import ceil

def CAR(Enum,grouping,gdat,elecs,bad_elecs):

    Ngroups = int(ceil(Enum/grouping)) #number of CAR groups
    
    #create grouping table containing list of electrode numbers per group
    groups = []
    for cnt in range(Ngroups):
        groups.append(np.array(range(int(grouping)))+(grouping*cnt))
    
    #remove any electrode number from grouping that is larger than Enum-1
    for i in groups[-1]:
        if i > Enum-1:
            groups[-1] = np.delete(groups[-1], list(groups[-1]).index(i))
    
    #remove bad electrodes from grouping table
    for i in range(len(groups)):
        if len(set(groups[i]) ^ set(bad_elecs)) < grouping:
            groups[i] = np.array(list(set(groups[i]) ^ set(bad_elecs)))
    
    #first subtract the mean from each good electrode
    for e in elecs:
        gdat[e-1] = gdat[e-1] - np.mean(gdat[e-1])
    
    #calculating group CARs
    CAR = []
    for cnt in range(Ngroups):
        CAR2 = np.array([0]*len(gdat[1])).astype(float)
        for a in groups[cnt]:
            CAR2 += gdat[a]
        CAR.append(CAR2)
        CAR[cnt] = CAR[cnt]/len(groups[cnt])
    
    #subtract group CAR from electrodes in group
    #calculate common CAR
    CAR_all = np.array([0]*len(gdat[1])).astype(float)
    for cnt in range(Ngroups):
        for a in groups[cnt]:
            gdat[a] = gdat[a] - CAR[cnt]
            CAR_all += gdat[a]
    CAR_all = CAR_all/len(elecs)

    #subtract common CAR from all good electrodes
    for e in elecs:
        gdat[e-1] = gdat[e-1] - CAR_all #remove total CAR from each electrode
    
    return gdat