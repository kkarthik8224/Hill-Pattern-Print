#!/usr/bin/env python
# coding: utf-8

# In[2]:


input1 = list()
num = int(input('Enter numbers in array: '))
for i in range(int(num)):
    n = input("num :")
    input1.append(int(n))
print ('Input: ',input1)
#3,1,2,3,6,2,3,6,2,3,6,3,2,3,6,5
# Find Max peak:
peak=0
peak_true=0
crest_true=0
for x in range(len(input1)):
    a=input1[x]
    if x%2==0:
        #print('adding')
        peak=peak+a
    else:
        #print("difference")
        peak=peak-a
        
    if peak_true<peak:
        peak_true=peak
    if crest_true>peak:
        crest_true=peak

#X_length
sum=0
for x in range(len(input1)):
    sum=sum+input1[x]
    
#print(sum)

#Western Ghats Schema-> Declaration of zero'es
array=[]
for i in range(peak_true-crest_true):
    row=[]
    for y in range(sum):
        row.append(0)
    array.append(row)
    
#westernghats Structure Build
origin_x=0
origin_y=peak_true-1
for x in range(len(input1)):
    a=input1[x]
    #print("input number",a," ",x)
    #print("x_origin_begin",origin_x+1)
    #print("Y_origin_begin",origin_y+1)
    if x%2==0:
        #print("uphill")
        for i in range(a):
            
            array[origin_y][origin_x]=1
            origin_x=origin_x+1
            origin_y=origin_y-1
            z=a-1
            if(i==z):
                origin_y=origin_y+1
    else:
        #print("downhill")
        for i in range(a):
            array[origin_y][origin_x]=-1
            origin_x=origin_x+1
            origin_y=origin_y+1
            z=a-1
            if(i==z):
                origin_y=origin_y-1
            
    #print("x_origin_ended",origin_x+1)
    #print("Y_origin_ended",origin_y+1)
        
#King On the mountain

p=array[0].index(1)+1
for i in range(p):
    print(" ",end="")
print("o")
for i in range(p-1):
    print(" ",end="")
print("/|",end="")
print("\\")
for i in range(p-1):
    print(" ",end="")
print("< >")
    
# Build my Western Ghats    
for x in array:
    i=0
    for k in x:
        if i==p:
            print(" ",end="")
        if k==0:
            print(" ",end="")
        if k==1:
            print("/",end="")
        if k==-1:
            print("\\",end="")
        i=i+1
        
    print()
#3,1,2,3,6,2,3,6,2,3,6,3,2,3,6,5


# In[ ]:




