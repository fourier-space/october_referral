"""
question3.py - image manipulation

You are provided with three images,
london.png, gradient.png, and mask.png
Which is a London skyline, a gradient, a mask for lettering.

a) Use matplotlib.pyplot to display - using plt.show() - a composited version of the image.
    I.e. the lettering mask in gradient colours overlaid on top of the skyline.

    Compositing is done pixel-wise, using the equation,
    c = m f + (1 - m) b
    where c is the composited output
    m is the mask value (between 0 and 1)
    f is the foreground pixel, and b is the background pixel.

b) Modify the mask so that the lettering is shifted vertically, 288 pixels,
    I.e. appears at the top of the image,
    Show the composited image with the new mask.

c) You are also provided with mayor.png, this is a mask for the lettering
    "Mayor of London", pad the mask so it is the same size as the base image
    and that the lettering appears in the bottom left.
    Composit the gradient on top of the previous result,
    using the padded "Mayor of London" mask and show() the outcome

Reference images of what your output should look like are provided in the references folder.

TOTAL POINTS AVAILABLE: 5 

Code Functionality (5)
a) 2 POINTS
b) 1 POINT
c) 2 POINTS
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
