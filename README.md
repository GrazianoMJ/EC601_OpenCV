# EC601_OpenCV
A tutorial assignment for the use of OpenCV as taught by Osama, Rashab, and Jinyuan

## Exercise 1:
*"How does a program read the cvMat object, in particula, what is the order of the pixel structure?"*- There are three main ways to access the data in the Mat object:
     1. Can use pointers and the [] indexing operator
     2. Can use a MatIterator object that can be incremented from beginning to end
     3. Can use the .at method which will directly access a particular row and column of the matrix.
- The pixel structure is dependent on the type of image:
     - Grayscale: Each pixel is represented by a single value (black to white). This means that each column of the matrix contains exactly one channel.
     - RGB: Each pixel is represented by three channels in the following order - Blue, Green, Red. This means that in order to scan over the matrix correctly, we must multiply the number of columns by the number of channels.

*Reference: [How to scan images, lookup tables and time measurement with OpenCV](https://docs.opencv.org/2.4/doc/tutorials/core/how_to_scan_images/how_to_scan_images.html#howtoscanimagesopencv)
