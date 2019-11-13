import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

image_size = 28 # width and length
#no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9
image_pixels = image_size * image_size
data_path = "mnist-in-csv/"
train_data=np.array(pd.read_csv(data_path + "mnist_train.csv"))
test_data=np.array(pd.read_csv(data_path + "mnist_test.csv"))

img = plt.imread("bir.png") #image loaded
plt.imsave("olusturulan.jpg",img,cmap="gray")
img = plt.imread("olusturulan.jpg") #gray image loaded


def func_pdf(x, mu=0.0, sigma=1.0): #pdf calculate function
    x = float(x - mu) / sigma
    return math.exp(-x*x/2.0) / math.sqrt(2.0*math.pi) / sigma
    

def func_counter(k=0):
	s=0
	for i in range(m):
		if(train_data[i,0]==k):
			s+=1
	return s


def func_mean_and_std(k=2,l=100):
	s=0
	t=0
	for i in range(m):
		if(train_data[i,0]==k):
			s+=1
			t+=train_data[i,l+1]
			digit_class=train_data[i,0]
			top_left=train_data[i,1]
			bottom_right=train_data[i,784]
	mean_1=t/s
	s=0
	t=0
	for i in range(m):
		if(train_data[i,0]==k):
			s+=1
			diff_1=train_data[i,l+1]-mean_1
			t+=diff_1*diff_1
	std_1=np.sqrt(t/(s-1))
	return mean_1,std_1








































