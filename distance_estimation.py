
# This file takes the center coordinates of the BB of the detected object.
# It plots the result of pixel intensity Vs number of pixels.
# Make sure to input the right RaDAR file corresponding to the camera file on which the YOLO is run.

import cv2
import numpy as np
import matplotlib.pyplot as plt
from AngleDiff_SciP import getAngle
import math
from skimage.measure import profile_line




def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    #print(type(ang))
    if ang < 0:
        angle_cam = -ang
        angle_rad = angle_cam/4
        plot_angle = 180 + angle_rad

    else:
        angle_cam = ang
        angle_rad = angle_cam / 4
        plot_angle = 180 - angle_rad

    #print(type(x))
    return plot_angle


def getline(center,angle,number_of_pixels):

    'Calculates the position of pixels as per the required angle'
    'Remember: x and y pixel values are inverted'
    'Input center coordinates as (y,x)'
    'It returns the values in the array form with y first and then x'

    y = np.cos(np.deg2rad(angle))
    x = np.sin(np.deg2rad(angle))

    y = y*np.arange(1,number_of_pixels) + center[0]
    x = x*np.arange(1,number_of_pixels) + center[1]

    return y , x


a = [] # empty array that takes the center points of the detected object BB

for i in range(0,2):
    ele = int(input('Enter coordinates of center of BB : '))

    a.append(ele)

plot_angle = getAngle((336, 0), (336, 376), (a[0], a[1]))
print('obj angle in cam: ',plot_angle)

#print(math.ceil(plot_angle))



line = (np.int32(getline([577,576], plot_angle, 600)))
print(line)

' make sure to insert the right Radar file here'


img_radar = cv2.imread("/home/shubham/Project_folder/yolo/Images/000001r_1c.png")
#cv2.line(img_radar,(576,577),(576,0),(0,0,255),1)
cv2.imshow('Radar Image',img_radar)
#cv2.line(img,(336,376),(336,0),(255,0,0),1)
#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('radar',img)

print(img_radar[line[0],line[1]])

intensity = img_radar[line[0],line[1]]
plt.plot(intensity, c = "green")
#plt.plot(intensity[:,1], c = "red")
#plt.plot(intensity[:,2], c = "red")
plt.xlabel('Number of pixels')
plt.ylabel('Pixel Intensities')
plt.show()



img_radar[line[0],line[1]] = [255,0,0]
plt.imshow(img_radar)
plt.show()
cv2.waitKey()



