Question 1 - XML-RPC image manipulation

The folder contains the following ipynb scripts:

1) XML-RPC server.ipynb, which contains code to start a server that receives an image from the client, saves it, performs 1 of 3 image manipulation methods as specified by the client, and saves the modified image. The 3 image manipulation methods are described below:

one: switching RGB channels to BRG, i.e. all the values in the Red channel are now in the Blue channel, all the values in the Green channel are now in the Red channel, and all the values in the Blue channel are now in the Green channel.

two: adding or subtracting a certain specified value from each channel. the user can specify different values for each channel to add or subtract. this number will be added to or subtracted from all values in the channel. values are entered as arguments via the client.

three: remove a certain specified channel, i.e. all the values of that particular channel are replaced with 0. the channel to remove is entered as an argument via the client.

2) XML-RPC client.ipynb, which contains code for a client that transmits an image and calls a desired image manipulation method over to the server, receives the modified image from the server and saves the modified image.

The following images are included:
-saturn_0026.jpg, the original original image
-image_original_client.jpg, saved by the client
-image_original_received_server.jpg, saved by the server
-image_switchedchannels_client.jpg manipulation method 1
-image_switchedchannels_server.jpg
-image_addsubtract_red-10_green-20_blue15_client.jpg manipulation method 2
-image_addsubtract_red-10_green-20_blue15_server.jpg
-image_remove_channel_red_client.jpg manipulation method 3
-image_remove_channel_red_server.jpg

Question 2 - Sound Files

This folder also contains the .ipynb script containing a module, FindNotes, that does the following:
-takes in the filename as an argument (an .aif file)
-plots the Amplitude of the sound file against time
-plots the Frequency spectrum (obtained via FFT)
-Calculates the number of peaks that are above a certain percentage of the major peak's power
-Calculates the peak frequency
-Calculates the major peak frequencies
-Returns the frequencies that are not harmonics (which should be the notes in the file)

FindNotes is also available as a .py script.

Note: This program is currently (as of now) unable to return the actual note name. This is doable by saving a dictionary of note names and frequencies, but the corresponding frequency for each note must have a certain range - they could possibly be integers, and the program will round the peak frequencies to the nearest integer and return its corresponding note name.