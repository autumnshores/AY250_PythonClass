import os
import sys
import time
from urllib import FancyURLopener
import urllib2
import simplejson
import matplotlib.pyplot as plt
import PIL
from PIL import ImageEnhance
import Image
import numpy as np
from numpy import sin, cos, linspace, pi
import wx
import matplotlib
# We want matplotlib to use a wxPython backend
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_wx import NavigationToolbar2Wx

try:
    from enthought.traits import *
    from enthought.pyface.api import GUI
    from enthought.traits.api import HasTraits, Int, Str, Button, Any, Instance
    from enthought.traits.ui.api import View, Item, ButtonEditor
    from enthought.traits.ui.wx.editor import Editor
    from enthought.traits.ui.wx.basic_editor_factory import BasicEditorFactory

except:
	from traits import *
	from pyface.api import GUI
	from traits.api import HasTraits, Int, Str, Button
	from traitsui.api import View, Item, ButtonEditor

class _MPLFigureEditor(Editor):
    
    scrollable  = True
    
    def init(self, parent):
        self.control = self._create_canvas(parent)
        self.set_tooltip()
    
    def update_editor(self):
        pass
    
    def _create_canvas(self, parent):
        """ Create the MPL canvas. """
        # The panel lets us add additional controls.
        panel = wx.Panel(parent, -1, style=wx.CLIP_CHILDREN)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)
        # matplotlib commands to create a canvas
        mpl_control = FigureCanvas(panel, -1, self.value)
        sizer.Add(mpl_control, 1, wx.LEFT | wx.TOP | wx.GROW)
        toolbar = NavigationToolbar2Wx(mpl_control)
        sizer.Add(toolbar, 0, wx.EXPAND)
        self.value.canvas.SetMinSize((10,10))
        return panel

class MPLFigureEditor(BasicEditorFactory):
    
    klass = _MPLFigureEditor


class ImageSearch(HasTraits):
    #define variables
    searchterm =  Str("What image would you like to see? Enter search query here.")
    showurl = Str()
    run_query = Button()
    figure = Instance(Figure, ())
    rotate_image = Button(label='Rotate 90 degrees cc')
    enhance_color = Button(label='Enhance color')
    shuffle = Button(label='Shuffle RGB channels')
    
    #function to display image ##problem here?
    def image_show(self, image):
        #Plots an image on the canvas in a thread safe way.

        self.figure.axes[0].images=[]
        self.figure.axes[0].imshow(image, aspect='auto')
        wx.CallAfter(self.figure.canvas.draw)

    #function to get URL of image, display and save image upon button press
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
    
        # Display image
        Im1 = plt.imread(str(self.searchterm)+'.jpg')
        image_show(Im1)


    #code to shuffle image RGB colors, display and save image upon button press
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
        image_show(Im2)
    
    #code to enhance image color by factor of 2, display and save image upon button press
    def _enhance_color_fired(self):
        array2 = plt.imread(str(self.searchterm)+'.jpg')
        img = Image.fromarray(array2)
        converter = PIL.ImageEnhance.Color(img)
        Im3 = converter.enhance(2.0)
        Im3.save(str(self.searchterm)+'_enhanced.jpg')
        image_show(Im3)
    
    #code to rotate image 90 degrees counter clockwise, display and save image upon button press
    def _rotate_image_fired(self):
        array3 = plt.imread(str(self.searchterm)+'.jpg')
        Im4 = Image.fromarray(array3)
        Im5 = Im4.rotate(90)
        Im5.save(str(self.searchterm)+'_rotated.jpg')
        image_show(Im5)
    
    #view variables
    view = View(Item('searchterm', label="Query string",
                 width=-600,resizable=True,padding=2),
            Item('run_query', show_label=False),
            Item('showurl', label="URL",
                  width=-600,resizable=True),
            Item('figure', editor=MPLFigureEditor(),
                     show_label=False,
                width=400,
                height=300,
                resizable=True),
            Item('rotate_image', show_label=False,
                  width=-200,resizable=True),
            Item('enhance_color', show_label=False,
                  width=-200,resizable=True),
            Item('shuffle', show_label=False,
                  width=-200,resizable=True))


ImageSearch().configure_traits()

