list=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a","a"]
i=0
a=[ ]
while i<len(list):
	j=0
	count=0
	b=[ ]
	while j<len(list):
		if list[i]==list[j]:
			count+=1
		j+=1
	b.append(list[i])
	b.append(count)
	if b not in a:
		a.append(b)
	i+=1
print(a,end="")