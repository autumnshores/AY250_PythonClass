import os
import sys
import time
from urllib import FancyURLopener
import urllib2
import simplejson
#from mpl_figure_editor import MPLFigureEditor
import matplotlib.pyplot as plt
import PIL
from PIL import ImageEnhance
import Image
import numpy as np

try:
	from enthought.traits import *
	from enthought.pyface.api import GUI
	from enthought.traits.api import HasTraits, Int, Str, Button
	from enthought.traits.ui.api import View, Item, ButtonEditor
except:
	from traits import *
	#from pyface.api import GUI
	from traits.api import HasTraits, Int, Str, Button
	from traitsui.api import View, Item, ButtonEditor

class ImageSearch(HasTraits):
    searchterm =  Str("What image would you like to see? Enter search query here.")
    showurl = Str()
    run_query = Button()
    rotate_image = Button(label='Rotate 90 degrees cc')
    enhance_color = Button(label='Enhance color')
    shuffle = Button(label='Shuffle RGB channels')
    def _run_query_fired(self):
        # Replace spaces ' ' in search term for '%20' in order to comply with request
        searchTerm = self.searchterm.replace(' ','%20')

        # Start FancyURLopener with defined version
        class MyOpener(FancyURLopener):
                version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
        myopener = MyOpener()
    
        url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+searchTerm+'&userip=MyIP')
        request = urllib2.Request(url, None, {'Referer': 'testing'})
        response = urllib2.urlopen(request)
    
        # Get results using JSON
        results = simplejson.load(response)
        data = results['responseData']
        dataInfo = data['results']
    
        # Get unescaped url
        self.showurl = str(dataInfo[0]['unescapedUrl'])
        
        # Save image
        myopener.retrieve(dataInfo[0]['unescapedUrl'],str(self.searchterm)+'.jpg')

    def _shuffle_fired(self):
        array = plt.imread(str(self.searchterm)+'.jpg')
        l,h,d = array.shape
        red = array[:,:,0]
        green = array[:,:,1]
        blue = array[:,:,2]
        array[:,:,0] = green
        array[:,:,1] = blue
        array[:,:,2] = red
        Im2 = Image.fromarray(array)
        Im2.save(str(self.searchterm)+'_shuffled.jpg')
    
    def _enhance_color_fired(self):
        array2 = plt.imread(str(self.searchterm)+'.jpg')
        img = Image.fromarray(array2)
        converter = PIL.ImageEnhance.Color(img)
        Im3 = converter.enhance(2.0)
        Im3.save(str(self.searchterm)+'_enhanced.jpg')
    
    def _rotate_image_fired(self):
        array3 = plt.imread(str(self.searchterm)+'.jpg')
        Im4 = Image.fromarray(array3)
        Im5 = Im4.rotate(90)
        Im5.save(str(self.searchterm)+'_rotated.jpg')
    

    view = View(Item('searchterm', label="Query string",
                 width=-600,resizable=True,padding=2),
            Item('run_query', show_label=False),
            Item('showurl', label="URL",
                  width=-600,resizable=True),
            Item('rotate_image', show_label=False,
                  width=-200,resizable=True),
            Item('enhance_color', show_label=False,
                  width=-200,resizable=True),
            Item('shuffle', show_label=False,
                  width=-200,resizable=True))

ImageSearch().configure_traits()

