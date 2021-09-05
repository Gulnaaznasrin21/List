numbers=[50,40,23,70,56,12,5,10,7]
i=0
max=0
while i<len(numbers):
    if max<numbers[i]:
        max=numbers[i]
    i+=1
print("maximum number is",max)
