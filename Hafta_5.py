import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math 

image_size = 28 # width and length
image_pixels = image_size * image_size
train_data=np.array(pd.read_csv("mnist_train.csv"))
test_data=np.array(pd.read_csv("mnist_test.csv"))

def pdf(x, mu=0.0, sigma=1.0):
    x = np.float32(x - mu) / (sigma+(1e+10))
    return np.exp(-x*x/2.0) / np.sqrt(2.0*math.pi) / sigma


def get_my_mean_and_std(k=2,l=100):
    #k=0
    s=0
    t=0
    #l=350
    for i in range(m):
        if(train_data[i,0]==k):
            s+=1

            t+=train_data[i,l+1]
            digit_class=train_data[i,0]
            top_left=train_data[i,1]
            bottom_right=train_data[i,784]
            #print(digit_class,end=" ")
            #print(top_left,end=" ")
            #print(bottom_right,end="\n")
    mean_1=t/s


    s=0
    t=0
    for i in range(m):
        if(train_data[i,0]==k):
            s+=1
            diff_1=train_data[i,l+1]-mean_1
            t+=diff_1*diff_1
    std_1=np.sqrt(t/(s-1))
    #var_1=t/(s-1)
    #print(mean_1,std_1)
    return mean_1,std_1

img = plt.imread("olusturulan.jpg")
'''
m,n,p=img.shape
#enbuyukpdf=0
enbuyukpdf1=0
sayi=0
for i in range(10):
    enbuyukpdf=1
    for j in range(m):
        for k in range(n):
            test_values=img[j,k]
            #print(test_values)
            m_1,std_1=get_my_mean_and_std(i,(28*j)+k)
            #print((28*j)+k)
            if (np.isnan(std_1)==False):
                if(std_1!=0.0):
                    #print("STD\n"+str(std_1))
                    pdf_deger=pdf(test_values,m_1,std_1)
                    if (np.isnan(pdf_deger)==False):
                        if (pdf_deger!=0.0):
                            #print("PDF\n"+str(pdf_deger))
                            #pdf_deger=math.log(pdf_deger)
                            enbuyukpdf+=pdf_deger
                            print(pdf_deger)

    if (enbuyukpdf1<enbuyukpdf):
        enbuyukpdf1=enbuyukpdf
        sayi=i
print("Değer")
print(sayi,enbuyukpdf1)'''



my_test_image1=plt.imread('manzara.jpg')
m,n,k=my_test_image1.shape

my_test_image=my_test_image1[:,:,0]
im_5=my_test_image.reshape(1, m*n)
plt.imshow(my_test_image)
plt.show()

my_list=[]
for i in range(10):
    pdf_t=0
    for j in range(784):
        x=im_5[0,j]
        m_1,std_1=get_my_mean_and_std(i,j)
        pdf_deger=my_pdf_1(x, m_1, std_1)
        pdf_t = pdf_t + pdf_deger
    print(pdf_t)
    my_list.append(pdf_t)

