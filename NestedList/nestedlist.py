x=[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
s=[]
for i in range(len(x)):
    s.append(x[i][1])
print(s)
y=max(s)
for i in range(len(s)):
    if s[i]==y:
        print(i)
x.pop(i)
print(x)
t=[]
for i in range(len(x)):
    t.append(x[i][1])
print(t)
u=max(t)
count=0
li=[]
for i in range(len(t)):
    if t[i]==u:
        count+=1
        print(count)
        li.append(i)
print(count)
