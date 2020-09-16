# Aligning-Prokudin-Gorskii-images

This project is derived from UMass Amherst CMPSCI Computer Vision Project.

Sergey Mikhaylovich Prokudin-Gorsky was a Russian chemist and photographer. He is known for his pioneering work in colour photography and his effort to document early 20th-century Russia. Using a railroad-car darkroom provided by Tsar Nicholas II, Prokudin-Gorsky traveled the Russian Empire from around 1909 to 1915 using his three-image colour photography to record its many aspects. (https://en.wikipedia.org/wiki/Sergey_Prokudin-Gorsky). Additonal negatives can be found on LOC website. (https://www.loc.gov/pictures/collection/prok/)

# Purpose
This project reproduce to the color photo by his RGB glass plate negatives. 
![alt text](https://github.com/YuchenZeng/Aligning-Prokudin-Gorskii-images/blob/master/images/example-Prokudin-Gorskii.png)

# Detail
Aligning image is easy. Minimizing the SSD Sum of Squared Differences(SSD) distance between the channels after randomly roll the image to match other. The result is not very good. 
![alt text](https://github.com/YuchenZeng/Aligning-Prokudin-Gorskii-images/blob/master/images/align.png)

A better way is to align the edge between each channel applying the Laplacian operator. 
![alt text](https://github.com/YuchenZeng/Aligning-Prokudin-Gorskii-images/blob/master/images/edge_detection.png)
![alt text](https://github.com/YuchenZeng/Aligning-Prokudin-Gorskii-images/blob/master/images/align_edge.png)
