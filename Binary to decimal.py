nums=[1,0,0,1,1,0,1,1]
nums.reverse()
a=nums
i=0
sum=0
while i<len(a):
    sum=(sum+a[i]*2**i)
    i+=1
print(sum)