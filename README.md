# EC601_OpenCV
A tutorial assignment for the use of OpenCV as taught by Osama, Rashab, and Jinyuan

## Exercise 1:
*"How does a program read the cvMat object, in particula, what is the order of the pixel structure?"*

- There are three main ways to access the data in the Mat object:
     1. Can use pointers and the [] indexing operator
     2. Can use a MatIterator object that can be incremented from beginning to end
     3. Can use the .at method which will directly access a particular row and column of the matrix.
- The pixel structure is dependent on the type of image:
     - Grayscale: Each pixel is represented by a single value (black to white). This means that each column of the matrix contains exactly one channel.
     - RGB: Each pixel is represented by three channels in the following order - Blue, Green, Red. This means that in order to scan over the matrix correctly, we must multiply the number of columns by the number of channels.

*Reference: [How to scan images, lookup tables and time measurement with OpenCV](https://docs.opencv.org/2.4/doc/tutorials/core/how_to_scan_images/how_to_scan_images.html#howtoscanimagesopencv)*

## Exercise 2:
1.*"ColorImage.cpp is a program that takes a look at colorspace conversions in OpenCV. Run the code in ColorImage.cpp and comment on the outputs. Implement the same thing in Python and save each image."*

- Each of the images created by the code are a single channel of the RGB, YCbCr, and HSV color models. These individual images are possible through the `split(<image>, vector<Mat>)` lines in each segment of the code.
     - Note that each picture other than the original is grayscale. This is due to the fact that by splitting the individual channels, we are creating a Mat object that has exactly one channel per pixel so we are ultimately creating a Grayscale Mat structure.
     - The RGB pictures show a great amount of detail due to the fact that each pixel is an additive component of Red, Green or Blue.
     - The YCbCr show us how the various segments of the picture contain more red or blue tones. For example, the feathers of the woman's hat in the Lenna.png file have a heavy amount of blue, hence why in the Cb picture, we see darker shading in that area versus the Cr picture where it is rather light.
     - The HSV file shows us how the Hue and Saturation pictures translate to the Value picture. We see that the Value picture is very light but when we look to the Hue and Saturation, we see the shadows and shading from the original picture follow the dark and light regions of the Hue and Saturation picture. 
