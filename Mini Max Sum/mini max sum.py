a=[1,2,3,4,5]
sum1=[]
for i in range(len(a)):
    n = a[:i] + a[i+1:]
    x=sum(n)
    sum1.append(x)
print(min(sum1), max(sum1))
