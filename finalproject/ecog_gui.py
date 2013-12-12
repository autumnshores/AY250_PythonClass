#ecog_gui.py

"""
This script will generate a GUI that allows the user to input key global information
about the particular dataset, load and view the analog speaker file, find and mark
the auditory events and load and view the electrode channels.

"""

import os
import sys
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.io
import find_aud_evs
from find_aud_evs import find_aud_evs


try:
    from enthought.traits import *
    from enthought.pyface.api import GUI
    from enthought.traits.api import HasTraits, Int, Str, Button, Any, Instance
    from enthought.traits.ui.api import View, Item, ButtonEditor
    #from enthought.traits.ui.wx.editor import Editor
    #from enthought.traits.ui.wx.basic_editor_factory import BasicEditorFactory

except:
	from traits import *
	from pyface.api import GUI
	from traits.api import HasTraits, Int, Str, Button
	from traitsui.api import View, Item, ButtonEditor


class ImageSearch(HasTraits):
    #define variables
    patientcode =  Str("Enter patient code, eg. CP1, ST2, GP3 etc.")
    taskname = Str("Enter task name, eg. passive, pitch, consonance etc.")
    totalelecs = Int("Enter total number of electrodes")
    srate = Str("Enter sampling rate")
    ANsrate = Str("Enter analog sampling rate")
    #figure = Instance(Figure, ())
    loadspkr = Button(label='Load and View analog speaker file')
    thresh = Int("Enter threshold number for finding auditory events")
    findaudevs = Button(label='Find and View auditory events')
    elec = Int("Enter electrode number to view")
    viewelec = Button(label='Load and View electrode')
    badelecs = Str("Enter bad electrodes separated by commas")
    ictal = Str("Enter list of ictal events, like this: [108,110], [200,201]")
    save_info = Button()

    
    #function to load and view analog speaker file upon button press
    def _loadspkr_fired(self):
        spkrmat = scipy.io.loadmat('spkr.mat')
        spkr = spkrmat['spkr'][0]
        plt.figure
        plt.plot(spkr)
        plt.title('speaker file plot')
        plt.xlabel('samples')
        plt.show()
    
    #function to find and view auditory events upon button press
    def _findaudevs_fired(self):
        spkrmat = scipy.io.loadmat('spkr.mat')
        spkr = spkrmat['spkr'][0]
        spkr = spkr - np.mean(spkr)
        thresh = self.thresh
        ansrate = self.ANsrate
        
        #finding auditory events
        t = find_aud_evs(spkr,thresh,ansrate,len(spkr))
        print t
        plt.figure
        plt.plot(spkr)
        plt.title('speaker file plot with marked auditory events')
        plt.xlabel('samples')
        for i in range(len(t)):
            plt.axvline(x=t[i][0], color = 'r')
            plt.axvline(x=t[i][1], color = 'k')
        plt.show()
    
    #function to load and view electrodes
    def _viewelec_fired(self):
        gdatmat = scipy.io.loadmat('gdat.mat')
        gdat = gdatmat['gdat']
        e = self.elec
        plt.figure
        plt.plot(gdat[e-1])
        plt.title('EEG plot for channel '+str(e))
        plt.xlabel('samples')
        plt.ylabel('microVolts')
        plt.show()
    
    #view variables
    view = View(Item('patientcode', label="Patient code",
                     width=-400,resizable=True,padding=2),
                Item('taskname', label="Task",
                     width=-400,resizable=True),
                Item('totalelecs', label="Total # of electrodes",
                     width=-400,resizable=True),
                Item('srate', label="EEG channel sampling rate",
                     width=-400,resizable=True),
                Item('ANsrate', label="Analog channel sampling rate",
                     width=-400,resizable=True),
                Item('loadspkr', show_label=False,
                     width=-400,resizable=True),
                Item('thresh', label="Threshold",
                     width=-400,resizable=True),
                Item('findaudevs', show_label=False,
                     width=-400,resizable=True),
                Item('elec', label="Electrode #",
                     width=-300,resizable=True),
                Item('viewelec', show_label=False,
                     width=-200,resizable=True),
                Item('badelecs', label="Bad electrodes",
                     width=-400,resizable=True),
                Item('ictal', label="Ictal epochs",
                     width=-400,resizable=True),
                Item('save_info', show_label=False))
                


ImageSearch().configure_traits()

