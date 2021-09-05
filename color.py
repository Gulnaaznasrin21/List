a=["0","1","2","3","4"]
b=["red","green","black","blue","white"]
c=["100","200","300","400","500"]
i=0
k=[]
while i< len(a) and len(b) and len(c):
	j=a[i]+b[i]+c[i]
	k.append(j)
	i+=1
print(k)