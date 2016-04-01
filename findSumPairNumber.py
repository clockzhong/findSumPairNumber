#! /usr/bin/env python
import sys
import os
import re


#get the number list
numberListStr=raw_input("Please input your number list (seperated by spaces)...\n")
numberList=[int(i) for i in numberListStr.split()]
print 'you have input the following number list:'
print numberList

#get the sum target value
sumTargetStr=raw_input("Please input your target number:\n")
sumTarget=int(sumTargetStr)
print 'your target is: '
print sumTarget


def generatePairsWith2IndexLists(list1, list2):
	result=[]
	for item1 in list1:
		for item2 in list2:
			#result.append([item1, item2])
			result.append([item1+1, item2+1])
	#print result
	return result

def generatePairsWithOneIndexLists(list1):
	result=[]
	index = 0
	while index< (len(list1)-1):
		index2=index+1
		while index2 < len(list1):
			#result.append([list1[index],list1[index2]])
			result.append([list1[index]+1,list1[index2]+1])
			index2+=1
		index+=1
	return result


def getPairs(numList, target):
	pairList=[]
	candidateSlots=[] ##we have (target-1) slots 

	#init the candidateSlots list
	index=0
	while index < target+1:
		candidateSlots.append(None)
		index+=1

	#generate the candidateSlots, contribute O(n) complexity
	index=0
	while index<len(numList):
		if numList[index]<=target and numList[index]>=0:
			#print 'index:',index
			#print 'numList[index]:',numList[index]		
			#print 'len(candidateSlots):',len(candidateSlots)
			if candidateSlots[numList[index]]==None:
				candidateSlots[numList[index]]=[index]
			else:
				candidateSlots[numList[index]].append(index)
		index+=1

	#print candidateSlots

	#generate the pairs list based on the candidateSlots[] we just created
	#contribute O(target) complexity
	index=0
	while index<=(target/2):
		if candidateSlots[index]!=None and candidateSlots[target-index]!=None:
			if index!=(target-index):
				newPairList=generatePairsWith2IndexLists(candidateSlots[index], candidateSlots[target-index])
			else:
				newPairList=generatePairsWithOneIndexLists(candidateSlots[index])
			pairList+=newPairList
		index+=1

	return pairList

print getPairs(numberList, sumTarget)

