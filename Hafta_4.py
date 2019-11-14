#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math
image_size = 28 # width and length
no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9
image_pixels = image_size * image_size
#train_data = np.loadtxt("mnist_train.csv", delimiter=",")
#test_data = np.loadtxt("mnist_test.csv", delimiter=",")
#test_data[:10]
train_data = np.loadtxt("mnist_train.csv", 
                        delimiter=",")
test_data = np.loadtxt("mnist_test.csv", 
                       delimiter=",")

#train_data[m,0] : sayının değerini verir devamı 28*28 lik görselin pixel değerleri
#ödev: girilen resmin değerini bul

image_size = 28
image_pixels = image_size * image_size

test_data[:10]

train_data.ndim, train_data.shape
train_data[10,0]

im_3=train_data[10,:]
im_3.shape
im_4=im_3[1:]
im_4.shape
im_5=im_4.reshape(28,28)
plt.imshow(im_5,cmap='gray')
plt.show()

m,n=train_data.shape
def my_counter(k=0):
    s=0
    for i in range(m):
        if (train_data[i,0]==3):
            s=s+1
    return s
for i in range(10):
    c=my_counter(i)
    print(i," ",c)


def my_pdf_1(x, mu=0.0, sigma=1.0):
    x = float(x - mu) / sigma
    return math.exp(-x*x/2.0) / math.sqrt(2.0*math.pi) / sigma
my_pdf_1(10,1,3)



for i in range(m):
    digit_class=train_data[i,0]
    top_left=train_data[i,1]
    bottom_right=train_data[i,784]
    print(digit_class,end=" ")
    print(top_left,end=" ")
    print(bottom_right,end=" ")


