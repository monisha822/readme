import cv2
import numpy as np
img=cv2.imread("C:\Users\monis\OneDrive\Pictures\graphics\nature.jpeg")
trans=np.float32([[1,0,50],[0,1,100]])
trans_img=cv2.warpAffine(img,trans(img.shape[1],img.shape[0]))
center=(img.shape[1]//2,image.shape)