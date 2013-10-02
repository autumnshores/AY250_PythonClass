Q2.ipynb contains code to extract 15 features from an image. The 15 features are:

1) Image size - returns a tuple containing the # of columns and # of rows
2) Rmean - the mean of the Red color channels
3) Gmean - the mean of the Green color channels
4) Bmean - the mean of the Blue color channels
5) Graymean - the mean of the grayscale color channels (created from RGB in appropriate proportions)
6) XCorrRG - the cross-correlation between the Red and Green channels, using scipy.signal.correlate2d in "valid" mode (originally used "same", but changed to "valid" to speed up processing time)
7) XCorrRB - the cross-correlation between the Red and Blue channels
8) XCorrGB - the cross-correlation between the Blue and Green channels
9) entropy - the proportion of pixels whose entropy is above a specified threshold (I specified 45)
10) hsobel - the proportion of pixels that are part of horizontal edges above a specified threshold (I specified 10.0)
11) vsobel - the proportion of pixels that are part of vertical edges above a specified threshold (I specified 10.0)
12) sober - the proportion of pixels that are part of edges (horizontal and vertical combined) above a specified threshold (I specified 10.0)
13) numobjects - the number of objects after image segmentation using watershed
14) numcorners - the number of corners in the image
15) numcontours - the number of contours in an image at a specified value (I specified 100)

Next part of code is stolen from hw_4machinelearningparallelstrawman.py, currently trying to incorporate all the feature extraction code into this but running into some problems.

I also included the skeleton code for the Random Forest Classifier, probably not going to have enough time to complete this but thought I'd include it in case I can get some partial credit maybe?