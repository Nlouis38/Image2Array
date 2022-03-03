# Convert image file to binary text program

import numpy as np                                          # imports numpy library use pip install opencv-python
import cv2                                                   # imports opencv library use pip install numpy

# Type into python terminal: pip install opencv-python
# ^ This is done to install syntax for cv2 (used within code)

# User inputs
img = cv2.imread(r"/Users/nazirlouis/Desktop/types-of-triangles-june112020-min.jpeg",2)  #converts image to grayscale
solenoid_delay = 0.02                                                                    #Solenoid firing delay in ms
solenoid_amount = 20                                                                     #amount of solenoids to use
width_ratio = 1                                                        #ratio to modify width of image (1 is no stretch)

# solenoid_amoount = height
# width_final = width

# Resizes image and converts to binary
width initial = solenoid_amount
width_final = width_initial * width_ratio

img = cv2.resize(img,(width,solenoid_amount))
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Displays grayscale and binary image
cv2.imshow("img",img)
cv2.imshow("Binary Image", bw_img)

# Converts binary image to matrix form
binary_img = np.zeros((width_final, solenoid_amount))                           # empty array
for i in range(width_final):                                           # nested for loop used to create matrix
    for j in range(solenoid_amount):
        pixel = bw_img[j, i]
        if pixel == 255:
            pixel = 0
            binary_img[i, j] = pixel                             # replaces value to matrix
        else:
            pixel = 1
            binary_img[i, j] = pixel                             # adds value to matrix
print(binary_img)                                                # shows matrix

# Assigns variable for each solenoid
solenoids = np.zeros(width_final)                                     # empty array
for i in range(width_final):                                          # loop that separates array into variables
    globals()['solenoids%s'%i] = binary_img[i]

cv2.waitKey(0)
cv2.destroyAllWindows()
