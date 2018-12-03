# Example Python Program for contrast stretching
import cv2
import numpy as np

def sharp(image):
	# Create sharpening kernel
	kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
			
	# applying the sharpening kernel to the input image & displaying it.
	sharpened = cv2.filter2D(image, -1, kernel)
	
	# Noise reduction
	sharpened = cv2.bilateralFilter(sharpened, 9, 75, 75) 
	return sharpened


# Create an image object
image = cv2.imread("./car.jpg")

cv2.imshow('original',image)

cv2_image = sharp(image)

cv2.imshow('sharp',cv2_image)

cv2.waitKey(0)