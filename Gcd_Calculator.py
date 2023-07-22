vl=[]
vl2=[]
vl3=[]
x=int(input('\nenter the numbers count: '))
for i in range(1,1+x):
    y=int(input('enter number: '))
    vl.append(y)
for j in range(len(vl)):
    for k in range(1,vl[j]+1):
        if vl[j]%k==0:
            vl2.append(k)
for w in range(len(vl2)):
    if (vl2.count(vl2[w]))==x:
        vl3.append(vl2[w])
print('GCD is:',max(vl3))
