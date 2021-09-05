num=[50,40,23,70,56,12,5,10,7]
i=0
max=0
second_max=0
while i<len(num):
    if max<num[i]:
        second_max=max
        max=num[i]
    if second_max<num[i] and num[i]<max :
        second_max=num[i]
    i+=1
print(second_max)