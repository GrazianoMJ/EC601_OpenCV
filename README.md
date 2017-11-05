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

2.*"Print out the values of the pixel at (20, 25) in the RGB, YCbCr, and HSV versions of the image. What are the ranges of the pixel values in each channel of each of the above mentioned colorspaces?"*
- **RGB Colorspace**: Each channel can be represented by a value from 0 to 255.
- **YCbCr Colorspace**: Depending on how the conversion of the color is done, each channel can range from 0-255 or 16-235.
- **HSV Colorspace**: Hue can represent a value between 0-360 (the angle of the hue), and Saturation/Value are represented by a percentage value between 0-100.

## Exercise 3:
1.*"Look at the code in Noise.cpp and implement the code in Python. Also, print the results for different noise values in the Gaussian case, mean = 0, 5, 10, 20 and sigma = 0, 20, 50, 100 and for the salt-and-pepper case, pa = 0.01, 0.03, 0.05, 0.4 and pb = 0.01, 0.03, 0.05, 0.4."*
2.*"Change the kernel sizes for all the filters with all different values for noises and print the results for 3x3, 5x5 and 7x7 kernels. Comment on the results. Which filter seems to work "better" for images with salt-and-pepper noise and gaussian noise?"*

- Using the Lenna.png sample image, I created a set of images using the combination of kernels and noise variables. These images are save in Exercise3_Output.
- Changing the Kernel size seems to blurring issues with the Gaussian Noise pictures (the larger the Kernel, the less clear the resulting image is).
- Changing the Kernel size does not seem to have a major affect on the image clarity for Salt & Pepper noise.
- The best filter for both Guassian & Salt-and-Pepper noise is the Median Filter (although it should be noted that eventually the noise can become so severe that the Median Filter is ineffective).
