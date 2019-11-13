#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
image_size = 28 # width and length
no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9
image_pixels = image_size * image_size
#train_data = np.loadtxt("mnist_train.csv", delimiter=",")
test_data = np.loadtxt("mnist_test.csv", delimiter=",")
test_data[:10]


#train_data[m,0] : sayının değerini verir devamı 28*28 lik görselin pixel değerleri
#ödev: girilen resmin değerini bul
