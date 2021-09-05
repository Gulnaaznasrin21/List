# find three pairs which sums are 
num=30
n=[10,11,12,13,14,15,17,18,19]
i=0
k=[]
while i<len(n):
    j=0
    while j<len(n)//2:
        if n[i]+n[j]==num:
            c=[n[i],n[j]]
            k.append(c)
        j+=1
    i+=1
print(k)