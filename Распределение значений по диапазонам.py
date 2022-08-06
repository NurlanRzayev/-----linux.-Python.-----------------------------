A=[3,5,7,8,1,9,4,1,4,8,
   9,5,2,4,7,2,1,5,3,6,
   2,3,6,6,7]

count_1_3=0
count_4_6=0
count_7_9=0

for x in A:
    if 1<=x<=3:
        count_1_3+=1
    elif 4<=x<=6:
        count_4_6+=1
    elif 7<=x<=9:
        count_7_9+=1

print('Range 1-3:',count_1_3,'items')
print('Range 4-6:',count_4_6,'items')
print('Range 7-9:',count_7_9,'items')