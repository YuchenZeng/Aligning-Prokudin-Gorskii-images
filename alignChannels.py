import numpy as np

import cv2
from matplotlib import pyplot as plt

method = 'SSD'

def alignChannels(img, max_shift):
    start = True
    image1 = img[:,:,0]
    image2 = img[:,:,1]
    image3 = img[:,:,2]
    
    '''
    # get the laplacian edge from the orignal image
    # remove noise
    img = cv2.GaussianBlur(img1,(3,3),0)
    # convolute with proper kernels
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y
    plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
    plt.show()
    '''
    img1 = Laplacian_edge(image1)
    img2 = Laplacian_edge(image2)
    img3 = Laplacian_edge(image3)
    
    x = img1.shape[0]
    y = img1.shape[1]
    best_shift1 = None
    best_shift2 = None
    best_diff1 = None
    best_diff2 = None
    for i in range(-max_shift[0],max_shift[1]+1):
        for j in range(-max_shift[0],max_shift[1]+1):
            # shift first image to match other two
            shift = [i,j]
            img1_f = np.roll(img1.copy(), [i, j], axis=[0, 1])
            
            diff1 = SSD(img1_f,img2)
            diff2 = SSD(img1_f,img3)
            if best_diff1==None:
                best_shift1=shift
                best_diff1=diff1
            if best_diff2==None:
                best_shift2=shift
                best_diff2=diff2
            
            if best_diff1>diff1:
                best_diff1 = diff1
                best_shift1=shift
            if best_diff2>diff2:
                best_diff2=diff2
                best_shift2=shift


    # inverse images
    imgs = np.zeros(img.shape)
    imgs[:,:,0] = image1
    imgs[:,:,1] = np.roll(image2,[-best_shift1[0],-best_shift1[1]],axis=[0,1])
    imgs[:,:,2] = np.roll(image3,[-best_shift2[0],-best_shift2[1]],axis=[0,1])

    shift_pred = np.array([best_shift1, best_shift2]).T
    
    return imgs,shift_pred
    # raise NotImplementedError("You should implement this.")

def SSD(img1, img2):
    diff = np.sum((img1-img2)**2)
    return diff

def Laplacian_edge(image):
    # remove noise
    img = cv2.GaussianBlur(image,(3,3),0)
    # convolute with proper kernels
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    return laplacian
