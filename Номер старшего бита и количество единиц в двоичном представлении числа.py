x=169
n=0
while x>0:
    x=x>>1
    n+=1
print('hight bit number=',n)

x=169
n1=0
while x!=0:
    k=x&1 #1=00000001
    if k==1:
        n1+=1
    x=x>>1
print('number of units=',n1)

x=169
n=0
n1=0
while x>0:
    n+=1
    k=x&1
    if k==1:
        n1+=1
    x=x>>1
print('hight bit number=',n,'number of units=',n1)