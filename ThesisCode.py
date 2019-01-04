##++++++++++++++++++++++++++++++++++++++++++++
from math import sin, cos, pi
from turtle import *
import time


##tracer(2,1)

totalNumberOfTest=sum(1 for line in open('UserTestResult.txt'));
firstTimePointSelect=False
x,y=0.0,0.0

def Conversion(NormalValueMax,NormalValueMin,ResultedValue):
    MaxValue = 0
    if (NormalValueMax > ResultedValue):
        MaxValue = NormalValueMax
        ResultedValue = (100*ResultedValue)/NormalValueMax
        NormalValueMax = 100
        
    else:
        MaxValue = ResultedValue
        NormalValueMax = (100*NormalValueMax)/ResultedValue
        ResultedValue = 100
        
    list = [NormalValueMax,NormalValueMin,ResultedValue]
    
    return list
def CalculateXYPoint(nextPoint):
    global firstTimePointSelect,x,y
    
    print('Total Number Of Test : ',totalNumberOfTest)
    if(totalNumberOfTest==1 and firstTimePointSelect==False):
        x=0;y=0;
        firstTimePointSelect=True
    elif(totalNumberOfTest==2 and firstTimePointSelect==False):
        x=-200;y=0;
        firstTimePointSelect=True

    elif(totalNumberOfTest>=3 and firstTimePointSelect==False):
        x=-500;y=-150;
        firstTimePointSelect=True
    else:
        x=x+2*nextPoint+10
        
    xyValue=[x,y]
    return xyValue

def DrawResult(nV,rV):
    if(nV>rV):
       xyList=CalculateXYPoint(nV)
    else:
       xyList=CalculateXYPoint(rV) 
    
    X=xyList[0];Y=xyList[1]
    ##print(X);print(Y)
    c1, c2 = 'red','green'
    ##    myCircle(0, 0, 200-i*40,c1, c2 )
    if(nV > rV):
        myCircle(X, Y, nV ,c1, c2 )
        ##c1, c2 = c2, c1
        myCircle(X, Y, rV, c1,c2 )
        c1,c2 =c2,c1

    else:
        myCircle(X, Y, rV ,c2, c1 )
        ##c2, c1 = c1, c2
        myCircle(X, Y, nV, c1, c2 )
        ##c2, c1 = c1, c2
    

def myCircle(x, y, r, c1, c2): # draw a circle with radius r in the point (x,y)
            up(); goto(x+r, y) ; down()
            color(c1, c2)
            begin_fill()
            for i in range(361):
                a = x + r*cos(pi*i/180)
                b = y + r*sin(pi*i/180)
                goto(a, b)
                ##print(a)
                ##print(b)
            end_fill()


##print(list)
##totalNumberOfTest=sum(1 for line in open('UserTestResult.txt'))
file=open("UserTestResult.txt","r")
for line in file:
    ##global totalNumberOfTest;
    
    SplitTest=line.split()
    print(SplitTest[0])
    nvMax=float (SplitTest[1])
    nvMin=float (SplitTest[2])
    resultValue=float (SplitTest[3])
    ##print(nvMax)
    ##print(nvMin)
    ##print(resultValue)
    list = Conversion(nvMax,nvMin,resultValue)
    nV1 = float (list[0])
    rV1 = float (list[2])
    print(nV1)
    print(rV1)
    DrawResult(nV1,rV1)
    
file.close()



