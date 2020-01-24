#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2


# In[3]:
def nothing(x):
    pass

cv2.namedWindow('threshold')
cv2.namedWindow('canny')

# add ON/OFF switch to "canny"
switch_c = '0 : OFF \n1 : ON'
switch_t = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch_c, 'canny', 0, 1, nothing)
cv2.createTrackbar(switch_t, 'threshold', 0, 1, nothing)


# add lower and upper threshold slidebars to "canny"
cv2.createTrackbar('lower', 'canny', 0, 255, nothing)
cv2.createTrackbar('upper', 'canny', 0, 255, nothing)

cv2.createTrackbar('value', 'threshold', 0, 255, nothing)
# cv2.createTrackbar('upper', 'threshold', 0, 255, nothing)



def sketch(image):
    # Convert image to grayscale
    
    return threshold


def capture():
    
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        image=frame
        

        
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
        # Clean up image using Guassian Blur
        img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)


        lower_c = cv2.getTrackbarPos('lower', 'canny')
        upper_c = cv2.getTrackbarPos('upper', 'canny')

        # lower_t = cv2.getTrackbarPos('value', 'threshold')
        upper_t = cv2.getTrackbarPos('value', 'threshold')

        s_c = cv2.getTrackbarPos(switch_c, 'canny')
        s_t = cv2.getTrackbarPos(switch_t, 'threshold')

        if s_c == 0:
            edges = img_gray
        else:
            edges = cv2.Canny(img_gray, lower_c, upper_c)

        if s_t == 0:
            threshold = edges
        else:
            ret,threshold = cv2.threshold(edges,0,upper_t,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
   


		
        cv2.imshow('original', image)
        cv2.imshow('canny', edges)
        cv2.imshow('threshold',threshold)
        k = cv2.waitKey(1) & 0xFF
        if k==13:
        	cv2.imshow("Final Sketch",threshold)
        	print("captured")
        	cv2.imwrite("./MySketch.jpg",threshold)
        elif k==27:
        	print("exit")
        	break


        	
    cap.release()
    cv2.destroyAllWindows()    
    
capture()
# try:
# 	capture()
# 	# print()
# except:
# 	print("Error")
# finally:
# 	cv2.destroyAllWindows()
	# if(cap!=null):
	# 	cap.release()
	# 	cv2.destroyAllWindows()				  
# In[4]:


# while True:
    
#     frame=capture();
#     op=sketch(frame)
    
#     if(cv2.waitKey(0)==13):
# #     confirm --> Enter
#         cv2.imwrite("MySketch.jpg",op)
#         break; 
        
#     elif(cv2.waitKey(0)==32):
#         cv2.destroyAllWindows()    
#         continue;
#     else:
#         break;
    
        
# cv2.destroyAllWindows()    




# In[ ]:




