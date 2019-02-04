#!/usr/bin/env python3

inp = input()
listNum = []
checkList=['0','1','2','3','4','5','6','7','8','9']
for i in inp:
	if i not in listNum:
		listNum.append(i)

listNum.sort()
notFound = []
print(listNum)
for j in checkList:
	if j not in listNum:
		notFound.append(j)
	
if len(notFound) == 0:
	print ("No missing digits")
else:
	print(*notFound)
