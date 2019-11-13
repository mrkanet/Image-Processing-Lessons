import os
import numpy as np
os.getcwd()
import matplotlib.pyplot as plt

def minimizePic(pic):
	m,n,p = pic.shape
	pic2 = np.zeros((int(m/2),int(n/2),3), dtype=int)
	new_m, new_n = int(m/2), int(n/2)

	for m in range(new_m):
		for n in range(new_n):
			s0 = (pic[m,n,0] + pic[m,n,1] + pic[m,n,2])/3
			s1 = (pic[m,n+1,0] + pic[m,n+1,1] + pic[m,n+1,2])/3
			s2 = (pic[m+1,n,0] + pic[m+1,n,1] + pic[m+1,n,2])/3
			s3 = (pic[m+1,n+1,0] + pic[m+1,n+1,1] + pic[m+1,n+1,2])/3
			s = (s0+s1+s2+s3)/4
			pic2[m,n] = s

	return pic2 

plt.imshow(minimizePic(plt.imread("manzara.jpg") ))
plt.show

def minimizeImg(img):
	m,n,p = img.shape
	new_m, new_n = int(m/2), int(n/2)
	new_img = np.zeros((new_m,new_n,3), dtype = int)

	for m in range(0,img.shape[0],2):
		for n in range(0,img.shape[1],2):
			s0 = (pic[m,n,0] + pic[m,n,1] + pic[m,n,2])/3
			s1 = (pic[m,n+1,0] + pic[m,n+1,1] + pic[m,n+1,2])/3
			s2 = (pic[m+1,n,0] + pic[m+1,n,1] + pic[m+1,n,2])/3
			s3 = (pic[m+1,n+1,0] + pic[m+1,n+1,1] + pic[m+1,n+1,2])/3
			s = (s0+s1+s2+s3)/4
			new_img[m,n] = int(s)
	return new_img

