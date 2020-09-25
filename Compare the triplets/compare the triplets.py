a=[5,6,7]
b=[3,6,10]
x,y=0,0
for i in range(3):
    if a[i]<b[i]:
        y+=1
    elif a[i]>b[i]:
        x+=1
    else:
        pass
print (x,y)
