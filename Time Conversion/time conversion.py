s='12:06:45PM'
s.split(":")
if int(s[0])<12:
    s[0] =str(int(s[0])+12)
elif int(s[0])==12:
    s[0]="00"
t=s[1:]
time=s[0]+t
print(time)
''' This is multi '''
