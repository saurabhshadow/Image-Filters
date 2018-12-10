import cv2
import numpy as np

class black_board:

	def __init__(self):
		pass
		
	def render(self,image):
		# Create sharpening kernel
		kernel = np.array([[1,-1,0], [-1,4,-1], [-1,0,-1]])

		# applying the sharpening kernel to the input image & displaying it.
		drawing = cv2.filter2D(image, -1, kernel)

		# Noise reduction
		drawing = cv2.bilateralFilter(drawing, 9, 75, 75) 
		return drawing

	

# Create an image object
image = cv2.imread("./farm.png")
tmp_canvas = black_board()
image = cv2.resize(image,(600,375))
res = tmp_canvas.render(image)
cv2.imwrite('black board drawing.jpg', res)
cv2.imshow('original',image)
cv2.imshow('black canvas',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
