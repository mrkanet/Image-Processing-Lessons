import matplotlib.pyplot as plt
import numpy as np

my_list_1=[2,4,3,4,5,6,3,3,2,1]
def my_function_1(my_list_1=[2,4,3,4,5,6,3,3,2,1]):
    t=0
    s=0
    for i in my_list_1:
        s=s+1
        t=t+i
    mean_1=t/s

    t=0
    s=0
    for i in my_list_1:
        s=s+1
        t=t+(i-mean_1)*(i-mean_1)
    var_1=t/(s-1)

    return mean_1,var_1
my_function_1()

my_histogram={}
for i in my_list_1:
    if i in my_histogram.keys():
        my_histogram[i]=my_histogram[i]+1
    else:
        my_histogram[i]=1
my_histogram



for i in my_histogram.keys():
    print(i,my_histogram[i])


image_1=plt.imread('truva.jpg')



def my_function_2(image_1=plt.imread('truva.jpg')):
    m,n,p=image_1.shape
    my_histogram={}
    for i in range(m):
        for j in range(n):
            if image_1[i,j,0] in my_histogram.keys():
                my_histogram[image_1[i,j,0]]=my_histogram[image_1[i,j,0]]+1
            else:
                my_histogram[image_1[i,j,0]]=1
    return my_histogram


def my_function_3(my_histogram=my_function_2()):
    x=[]
    y=[]
    for key in  my_histogram.keys():
        x.append(key)
        y.append(my_histogram[key])
    return x,y

x,y=my_function_3()
plt.bar(x,y)
plt.show()
