Final Project

You should find the following files in the package:

iPython Notebook
- Final Project.ipynb

.py scripts
- ecog_gui.py
- find_aud_evs.py
- CAR.py
- create_spect.py

data files
- gdat.mat: the file containing the EEG dataset (WARNING: BIG FILE! but it's already the smallest dataset that I have)
- spkr.mat: the file containing the speaker file that contains a record of the stimuli played during the experiment (musical chords in my case)
- CP5_passive_block2.xls: the file containing a list of the names of the stimuli in the order that they were played

For my final project, my goal was to re-program my ECoG data pre-processing and analysis in python (originally done in Matlab). The steps taken are documented in the .ipynb file, and this file should be opened first.

My task: The patient is passively listening to musical chords with some distractor sounds (cat meows).

Lecture themes used: GUIs, pandas, some tools from matplotlib and scipy 


The steps are as follows:

Step 1: enter global information of dataset
- patient code, task name, sampling rate, analog sampling rate, number of electrodes, bad electrodes, ictal epochs

Step 2: load and view the analog speaker file

Step 3: find auditory events from speaker file
- mark the onset and offset times of the stimuli

Step 4: load and view the electrode channels

Step 5: common average reference (CAR)

Step 6: generate spectrograms

Step 7: create events dataframe
- assemble a data structure containing the stimulus name, stimulus type (chord vs. distractor sound), onset time, offset time, whether it is a bad event.

Step 8: create surrogate data for statistical analysis (incomplete)

Step 9: create analysis event-related spectral perturbations (ERSPs) using the surrogate data (incomplete)

Step 10: plot ERSPs (incomplete)



Steps 1-4 involve loading and visualizing data, hence I made them available in both GUI format as well as in the ipynb. My original goal was to create a python-equivalent version of EEGplot in matlab, which is a GUI that will let the user load in the entire EEG dataset and visualize all the channels at one go in order to manually identify bad electrodes and ictal epochs. The user can adjust the number of channels to display, as well as the length of data to display (e.g. show 5 seconds of it at one time, and allow the user to scroll through the dataset in 5-second blocks). However, that proved to be a little too ambitious for this project, I spent way too much time trying to re-create it and failed miserably :(. In the end, what is presented here is a very simple version of loading and viewing 1 electrode at a time.

Steps 5-6 involve re-writing several scripts that I wrote in matlab. This took -alot- more time than I had anticipated. However, in the process of doing so, I was able to make both my scripts (this one in python and my original one in matlab) more efficient, and I gained a better understanding of what functions work better/faster in matlab and in python.

Step 7 employs the pandas dataframe, and associates the stimuli names and types with the onset and offset times calculated in Step 3. It also marks the events that are bad (e.g. occurred within an ictal epoch), and allows me to sort and select the stimuli and times based on different criteria. I very much prefer this over the matlab data structures that I am currently using - I was able to do what took me 10+ lines in matlab in just 1 line here. Pandas is awesome!

Steps 8-10 involve re-writing more scripts that I wrote in matlab, and they are still in progress (a bug in Step 6 is currently hindering progress in these steps, detailed below).



**CURRENT STATUS** 
There are bugs in the following areas:
- ecog_gui.py -> i upgraded my Mac OS system after completing the homework on GUIs, so I started having problems with visualizing figures within the GUI using Traits. This is the main reason why my efforts to try and recreate the EEGplot visualization GUI failed miserably. However, the code I submitted here still generates the graphs but it takes time to load (~7 secs), and they appear outside the GUI window. So it looks like the program is hanging, but it's not!

- create_spect.py script (used in Step 6: generate spectrograms) --> one part of the script is currently broken: one of the functions in the script (my_hilbert) breaks within the loop, I have found the source of the problem and am currently trying to fix it, but it is taking much longer than I expected and I may not be able to fix this in time. However, it does not affect Step 7.