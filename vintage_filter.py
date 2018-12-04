import cv2
class vintageFilter:

    def __init__(self):
        pass

    def render(self, img_rgb):
        img_rgb = cv2.imread(img_rgb)
        img_rgb = cv2.resize(img_rgb, (1024,600))
        img_color = img_rgb
        
        newImage = img_color.copy()
        i, j, k = img_color.shape
        for x in range(i):
            for y in range(j):
                R = img_color[x,y,2] * 0.393 + img_color[x,y,1] * 0.769 + img_color[x,y,0] * 0.189
                G = img_color[x,y,2] * 0.349 + img_color[x,y,1] * 0.686 + img_color[x,y,0] * 0.168
                B = img_color[x,y,2] * 0.272 + img_color[x,y,1] * 0.534 + img_color[x,y,0] * 0.131
                if R > 255:
                    newImage[x,y,2] = 255
                else:
                    newImage[x,y,2] = R
                if G > 255:
                    newImage[x,y,1] = 255
                else:
                    newImage[x,y,1] = G
                if B > 255:
                    newImage[x,y,0] = 255
                else:
                    newImage[x,y,0] = B

        return newImage

tmp_canvas = vintageFilter()
file_name = "car.jpg" #File_name will come here
res = tmp_canvas.render(file_name)
cv2.imwrite("BW1 version.jpg", res)
cv2.imshow("BW1 version", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
