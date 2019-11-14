import numpy as np
import matplotlib.pyplot as plt



def my_function_1(my_list=[9,3,5,6,2,5,6]):
    for i in range(len(my_list)):
        my_list[i]=my_list[i]+1
    print(my_list)
my_function_1()

def my_function_2(my_array=np.array(list([9,3,5,6,2,5,6]))):
    return my_array+10
my_function_2()

im_1=plt.imread('istanbul.jpg')
plt.imshow(im_1)
plt.show()

m,n,p=im_1.shape
im_2=np.zeros((m,n,3),dtype=int)
m,n,im_2.shape
for m in range(im_1.shape[0]):
    for n in range(im_1.shape[1]):
        im_2[m,n,0]=im_1[m,n,0]-25   #R bantını 25 eksiltiyor 
        im_2[m,n,1]=im_1[m,n,1]
        im_2[m,n,2]=im_1[m,n,2]
plt.imshow(im_2)
plt.show()

m,n,p=im_1.shape
im_2=np.zeros((m,n,3),dtype=int)
m,n,im_2.shape
for m in range(im_1.shape[0]):
    for n in range(im_1.shape[1]):
        im_2[m,n,0]=im_1[m,n,0]-25   #R bantını 25 eksiltiyor 
        im_2[m,n,1]=im_1[m,n,1]
        im_2[m,n,2]=im_1[m,n,2]
plt.imshow(im_2)
plt.show()

def my_function_3(im_100,s):
    im_1=im_100
    m,n,p=im_1.shape
    im_2=np.zeros((m,n,3),dtype=int)
    m,n,im_2.shape
    for m in range(im_1.shape[0]):
        for n in range(im_1.shape[1]):
            im_2[m,n,0]=im_1[m,n,0]-s   #R bantını 25 eksiltiyor 
            im_2[m,n,1]=im_1[m,n,1]
            im_2[m,n,2]=im_1[m,n,2]
    return im_100

def my_function_4(im_500):
    m,n,p=im_500.shape
    new_m=int(m/2)
    new_n=int(n/2)
    im_600=np.zeros((new_m,new_n),dtype=int)

    for m in range(new_m):
        for n in range(new_n):
            s0=(im_500[m*2,n*2,0]+im_500[m*2,n*2,1]+im_500[m*2,n*2,2])/3 #bulunulan piksel
            im_600[m,n]=int(s0)
    return im_600

im_6=my_function_4(im_1)
plt.imshow(im_6,cmap='gray')
plt.show()
plt.imsave('istanbulGray.jpg',im_6,cmap='gray')

def my_scale(im_7):
    m,n,p=im_7.shape
    new_m=int(m/2)
    new_n=int(n/2)
    im_8=np.zeros((new_m,new_n,3),dtype=int)
    for m in range(new_m):
        for n in range(new_n):
            im_8[m,n,0]=int(im_7[m*2,n*2,0])
            im_8[m,n,1]=int(im_7[m*2,n*2,1])
            im_8[m,n,2]=int(im_7[m*2,n*2,2])
    return im_8

im_10=my_scale(im_1)
plt.imshow(im_10)



im_100=my_scale(im_10)
plt.imshow(im_100)


