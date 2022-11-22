import cv2
import numpy as np
from matplotlib import pyplot as plt
p1=cv2.imread('opencv.png')
#plt.imshow(p1)
p1=cv2.cvtColor(p1,cv2.COLOR_RGB2BGR)
#plt.imshow(p1)
ke=np.ones((4,4))/25
img=cv2.filter2D(src=p1,ddepth=-1, kernel=ke)
plt.imshow(img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imwrite("image.jpg",img)
