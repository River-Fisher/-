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
def getTransArrSML(sumfreq,setfreq):
    setfreq = np.array(setfreq)
    setfreq = setfreq.reshape(setfreq.size//2,2)
    TransArrSML = np.zeros(256,int)
    for i in range(0,256):
        for j in range(0,setfreq.shape[0]):
            if(j==setfreq.shape[0]-1):
                TransArrSML[i]=setfreq[j][0]
                break
            if np.abs(sumfreq[i]-setfreq[j][1])>np.abs(sumfreq[i]-setfreq[j+1][1]):
                continue
            else:
                TransArrSML[i]=setfreq[j][0]
                break
    return TransArrSML


filename = "安徽-宣城敬亭山石桥.jpg"
sourceImg  = Image.open(filename)
r,g,b = sourceImg.split()
setfreq = [1,0.1,11,0.2,21,0.3,31,0.4,41,0.5,80,0.6,160,0.7,220,0.9,255,1]

freqnum = getfreqnum(np.array(r))
freq = getfreq(freqnum,sourceImg.size[1]*sourceImg.size[0])
sumfreq = getsumfreq(freq)
TransArrSML =getTransArrSML(sumfreq,setfreq)
rPicNum = np.array(r)
rPicNum = rPicNum.reshape(rPicNum.size)
newPicNum = np.zeros(rPicNum.size,'int')
for i in range(rPicNum.size):
    newPicNum[i] = TransArrSML[rPicNum[i]]
newimgR = Image.fromarray(newPicNum.reshape(sourceImg.size[1],sourceImg.size[0]))

freqnum = getfreqnum(np.array(g))
freq = getfreq(freqnum,sourceImg.size[1]*sourceImg.size[0])
sumfreq = getsumfreq(freq)
TransArrSML =getTransArrSML(sumfreq,setfreq)
gPicNum = np.array(g)
gPicNum = gPicNum.reshape(gPicNum.size)
newPicNum = np.zeros(gPicNum.size,'int')
for i in range(gPicNum.size):
    newPicNum[i] = TransArrSML[gPicNum[i]]
newimgG = Image.fromarray(newPicNum.reshape(sourceImg.size[1],sourceImg.size[0]))

freqnum = getfreqnum(np.array(b))
freq = getfreq(freqnum,sourceImg.size[1]*sourceImg.size[0])
sumfreq = getsumfreq(freq)
TransArrSML =getTransArrSML(sumfreq,setfreq)
bPicNum = np.array(b)
bPicNum = bPicNum.reshape(bPicNum.size)
newPicNum = np.zeros(bPicNum.size,'int')
for i in range(bPicNum.size):
    newPicNum[i] = TransArrSML[bPicNum[i]]
newimgB = Image.fromarray(newPicNum.reshape(sourceImg.size[1],sourceImg.size[0]))


newimg = Image.merge('RGB',(newimgR.convert('L'),newimgG.convert('L'),newimgB.convert('L')))
newimg.save("彩色SML后"+filename)







