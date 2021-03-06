# Single Layer Neural Network

Project description: http://ranger.uta.edu/~kamangar/CSE-5368-FA18/Assignment03(Duedate.Oct.7,2018).html

### __Description:__  
__Single layer Neural Network with 10 nodes to identify the MNIST dataset.__  
The purpose of the this assignment is to practice with `Hebbian learning rules`.
 Write a program to implement a single layer neural network with `10 nodes.`

 
Your program should include 1 sliders, 2 buttons, and 2 drop-down selection box.
 
### __Slider:__
- __"Alpha (learning rate)".__ - `Range should be between 0.001 and 1.0.` Default value = 0.1

### __Buttons:__
- __"Adjust Weights (Learn)".__ When this button is pressed the selected `Hebbian learning rule` should  be applied for `100 epochs.`
- __"Randomize Weights".__ When this button is pressed weights and biases should be randomized. The value of the randomized weights and biases should be from `-0.001 to 0.001.`
- __"Display Confusion Matrix".__ When this button is pressed the confusion matrix for the test set should be displayed.

 
### Drop-Down Selection Boxes- 
- __"Select Learning Method".__ A drop-down box to select one of the three Hebbian rules from your textbook, `i.e. "Filtered Learning (Smoothing)", "Delta Rule", or "Unsupervised Hebb".`
- __"Transfer Functions".__ A drop-down box to allow the user to select between three transfer functions `(Symmetrical Hard limit, Hyperbolic Tangent, and Linear)`

### Notes:

- [x] Put all the mnist image files in a directory called "Data". This directory should be located in the same folder as your main program. When submitting your assignment you do not need to submit the mnist images.
- [x] When your program starts it should automatically read the mnist data. Once the mnist data is read your program should convert each image to a vector and normalize each vector element to be in the range of -1 to 1. i.e. , divide the input numbers by 127.5 and subtract 1.0. Notice that normalizing each element of a vector to be between `-1 to 1` does not normalize the vector itself.
- [x] When your program starts it should automatically initialize all the weights and biases to be from -`0.001 to 0.001`
- [x] When your program starts it should automatically separate the input data into two sets. The first set should include 80% of your data set (randomly selected). This is your training set. The second set (the other 20%) is the test set. The test set will be used for calculating the error rate and the confusion matrix.
- [x] The index of the maximum value of the output vector is selected as the class id.
- [x] Plot the error rate, in percent, after each epoch on the error rate graph. An epoch is one pass over all the training samples. This means that you train (adjust the weights) for one complete set of the training data (one epoch). Then turn off the training (freeze the weights and biases) and run the test data through the network and calculate the error rate
- [x] The error graph should be plotted as percent error.
- [x] The error-rate graph should be able to display up to `1000 epochs.`
- [x] If you are using python, your assignment should run on `Python 3.x`
- [x] Make sure that you follow the submission guidelines to submit your code to Blackboard.
