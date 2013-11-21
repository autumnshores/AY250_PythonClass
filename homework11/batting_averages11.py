# batting_averages.py

"""
A model for calculating batting averages

"""

import pymc
import numpy as np
import pandas as pd

# load in data
D = pd.read_csv('laa_2011_april.txt',delimiter='\t')
N = D['G'] #at bats variable
num_hits = D['R'] #num of hits variable

#note: method for calculating alpha and beta is detailed in the readme
alpha = 43.78
beta = 127.92
#nplayers = 13

#mus = np.empty(nplayers)
#xs = np.empty(nplayers)

#for i in np.arange(nplayers):
# prior on mu_i
mu = pymc.Beta('mu', alpha, beta)

# likelihood
x = pymc.Binomial('x', n=N[10], p=mu, value=num_hits[10], observed=True)
