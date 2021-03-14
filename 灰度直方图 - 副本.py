from matplotlib import pyplot as plt 
from PIL import Image
import numpy as np

def freqnum(arr):
    arr = arr.reshape(arr.shape[0]*arr.shape[1])
    freq = np.zeros(256,int)
    for i in arr:
        freq[i] +=1
    
    return freq


filename = "SML均衡后安徽-宣城敬亭山石桥.jpg"
sourceImg  = Image.open(filename)
r,g,b = sourceImg.split()
freq = freqnum(np.array(r))

x = np.arange(0,256)
plt.figure(1,figsize=(16,10))
plt.stem(x,freq)
plt.savefig('直方图'+filename)
