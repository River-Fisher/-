from matplotlib import pyplot as plt 
from PIL import Image
import numpy as np



def getfreqnum(arr):
    arr = arr.reshape(arr.shape[0]*arr.shape[1])
    freq = np.zeros(256,int)
    for i in arr:
        freq[i] +=1   
    return freq

def getfreq(freqnum,count):
    return freqnum/count
def getsumfreq(freq):
    sumfreq = np.zeros(256,float)
    sumfreq[0] = freq[0]
    for i in range(1,256):
        sumfreq[i] = sumfreq[i-1]+freq[i]
    return sumfreq
def getTransArr(sumfreq):
    TransArr = np.zeros(256,int)
    for i in range(0,256):
        TransArr[i] = int(255*sumfreq[i]+0.5)
    return TransArr
filename = "安徽-宣城敬亭山石桥.jpg"
sourceImg  = Image.open(filename)
r,g,b = sourceImg.split()

freqnum = getfreqnum(np.array(r))
freq = getfreq(freqnum,sourceImg.size[1]*sourceImg.size[0])
sumfreq = getsumfreq(freq)
TransArr = getTransArr(sumfreq)
rPicNum = np.array(r)
rPicNum = rPicNum.reshape(rPicNum.size)
newPicNum = np.zeros(rPicNum.size,'int')
for i in range(rPicNum.size):
    newPicNum[i] = TransArr[rPicNum[i]]
newimgR = Image.fromarray(newPicNum.reshape(sourceImg.size[1],sourceImg.size[0]))

freqnum = getfreqnum(np.array(g))
freq = getfreq(freqnum,sourceImg.size[1]*sourceImg.size[0])
sumfreq = getsumfreq(freq)
TransArr = getTransArr(sumfreq)
gPicNum = np.array(g)
gPicNum = gPicNum.reshape(gPicNum.size)
newPicNum = np.zeros(gPicNum.size,'int')
for i in range(gPicNum.size):
    newPicNum[i] = TransArr[gPicNum[i]]
newimgG = Image.fromarray(newPicNum.reshape(sourceImg.size[1],sourceImg.size[0]))

freqnum = getfreqnum(np.array(b))
freq = getfreq(freqnum,sourceImg.size[1]*sourceImg.size[0])
sumfreq = getsumfreq(freq)
TransArr = getTransArr(sumfreq)
bPicNum = np.array(b)
bPicNum = bPicNum.reshape(bPicNum.size)
newPicNum = np.zeros(bPicNum.size,'int')
for i in range(bPicNum.size):
    newPicNum[i] = TransArr[bPicNum[i]]
newimgB = Image.fromarray(newPicNum.reshape(sourceImg.size[1],sourceImg.size[0]))


newimg = Image.merge('RGB',(newimgR.convert('L'),newimgG.convert('L'),newimgB.convert('L')))
newimg.save("彩色均衡后"+filename)




    
        
        

