import numpy as np
import cv2


def Distortion(img,distCoeff,pos):
    centx=pos[0]
    centy=pos[1]
    cam =np.array ([[10 ,0.0  ,centx],   #width/2.0 move image to origin
                   [0.0 ,10   ,centy],
                   [0.0 ,0.0   ,1.0       ]])
    
    # Remove Distortion with Distortion
    out = cv2.undistort(img,cam,distCoeff)
    
    return out
    


if __name__=='__main__':
    src    = cv2.imread("D:\\img.png")
   
    
    # TODO: add your coefficients here!
    k1 = -1e-4; # positive to add barrel distortion
    k2 = 0;
    p1 = 0;      # if there has no tangential lens distortion set p to zero
    p2 = 0;
    k3 = 0#12;
    
    distCoeff=(k1,k2,p1,p2,k3)
    
    width  = src.shape[1]  # Default,you can change it to any numbers.
    height = src.shape[0]
    pos=[width/2,height/2]
    
    out=Distortion(src, distCoeff,pos)
    
    cv2.imshow('out',out)
    cv2.waitKey()
    cv2.destroyAllWindows()
    