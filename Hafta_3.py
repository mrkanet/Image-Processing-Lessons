#bu derste listeler ile işlemler yapıldı
import os
import numpy as np
os.getcwd()
import matplotlib.pyplot as plt

def myfunc2 (myArray = np.array(1,2,3,4,5,6)):
	return(myArray+10)


img = plt.imred("manzara") 
#plt.imshow(img)
#plt.show()

print(img.ndim, img.shape)

#m,n,p = img.shape
#img2 = np.zeros((m,n,3), dtype = int)
#for j in range(img.shape[0]):
#	for i in range(img.shape[1]):
#		img2[m,n,0] = img[j,i,0] + 25


def minimizePic(pic):
	m,n,p = pic.shape
	pic2 = np.zeros((m/2,n/2), dtype=int)
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
