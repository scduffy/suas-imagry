# SUAS-Imagry

## Idea
Instead of building a neural network or some other expensive AI type program to detect and identify targets, instead a series of filters makes it easy to parse shapes out of an image and identify them. A user can then identify the mistakes of the software and add the additional required data pieces for submission and grading.

## Steps
The first step of image recognition is the filtering out of colors that the targets will likely not be. Knowing that the targets will be sitting in a field of uniform color, be it green if grass or gray if concrete, the first filter would filter out those colors and replace with a solid black background making the target objects stand out strongly. This sharp contrast of the color of the targets and the enviroment makes it easy for the next filter, shape detection, to determine the shapes of the targets as it relies on edge detection. 
