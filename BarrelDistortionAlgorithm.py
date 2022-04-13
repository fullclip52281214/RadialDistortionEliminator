import cv2
import numpy as np
import math

img = cv2.imread("img.png") #Img size must be 1280*720
h,w,d=img.shape


k1=1e-6  #6
k2=0 #11
k3=0 #16


castx=np.zeros((h,w),dtype=np.float32)
casty=np.zeros((h,w),dtype=np.float32)

for y in range(h):
    for x in range(w):
        r=math.sqrt((x-640)**2+(y-360)**2)
        castx[y,x]=((x-640)*(1+k1*r**2+k2*r**4+k3*r**6))+640
        casty[y,x]=((y-360)*(1+k1*r**2+k2*r**4+k3*r**6))+360
        
        
newimg=cv2.remap(img,castx,casty,cv2.INTER_LINEAR) #根據新座標所需從原圖抓取表中數值


''' #remap is faster
for y in range(h):
    for x in range(w):
        r=math.sqrt((x-640)**2+(y-360)**2)
        castx=int((x-640)*(1+k1*r**2+k2*r**4+k3*r**6))+640
        casty=int((y-360)*(1+k1*r**2+k2*r**4+k3*r**6))+360
        
        if(castx<w and castx>=0 and casty<h and casty>=0): #將原圖映射至新圖
            newimg[casty,castx,0:3]=img[y,x,0:3]
'''

cv2.imshow("newimg",newimg)

cv2.waitKey()
cv2.imwrite("out.png",newimg)
cv2.destroyAllWindows()