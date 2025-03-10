#1 missed value

lis = [1,2,8,4,10,6]
lis.sort()

for i in range(1,max(lis)+1):
    if i not in lis:
        print(i)


#2 avg in list


lis = [2,4,5,6,7,8]
num = len(lis)

sum_lis = 0
avg_lis = 0

for i in lis:
    sum_lis = i + sum_lis
    avg_lis = sum_lis / num

print(avg_lis)



#3 find negative number

lis = [1,3,4,5,-1,-3]


for i in lis:
    if i<0:
        print(i)














