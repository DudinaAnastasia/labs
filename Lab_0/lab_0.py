f=open('task1.txt','r')
lst=[]
for line in f:
	lst.append(int(line))
	lst.sort()
	minNum=min(lst)
	maxNum=max(lst)
	print ("\nСообщение "+str(minNum)+ "-"+str(maxNum)+" ",end="")

	if maxNum-minNum==len(lst)-1:
		print("полученно полностью",end=" ")
	else:
		print("не хватает пактов",end=" ")
		k=0
		for i in range(minNum + 1,maxNum):
			for j in range(k,len(lst)):
				if i==lst[j]:
					break
				if i<lst[j]:
					if i !=minNum+1:
						print(",",end="")
					print(i,end="")
					k=j
					break
print(".")
