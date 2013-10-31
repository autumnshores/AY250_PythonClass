Homework 8

imagesearch.py creates a GUI that grabs an image from the internet based on specified search terms, displays the image, and allows the user to perform 3 types of image manipulation functions, displaying the generated image. Specifically, it:

1. Takes in an input string in the 'query string' box

2. Upon pressing the button "Run query", it will:
   a) load the URL of the first image that appears in the Google search engine in the "URL" line
   b) display the image below the URL (**currently in progress - I am having extreme difficulty installing wxPython onto my mac but I was JUST able to get it to work on a Windows machine, so updates to the code will follow shortly)
   c) saves the image to the folder

3. Below the image display are 3 buttons that will each perform an image manipulation:
   a) Rotate 90 degrees cc - rotates the image 90 degrees counter-clockwise
   b) Enhance color - enhances image color by a factor of 2
   c) Shuffle RGB channels - reorders the image array matrix such that RGB becomes GBR
   Each button will also display the generated image (currently in progress) and save the generated image to the folder.


Latest update: the figure canvas loads fine, but i am having trouble with the function image_show that displays the image after pulling the URL.