#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'George Cui'

class Stu:
	def __init__(self, number):
		self.number = number
		self.score = '0'

	def setName(self, name):
		self.name = name

	def setScore(self, score):
		self.score = score

	def __str__(self):
		return self.number + ' ' + self.name + '   ' + self.score

def writescores(stus, resultfile):
	result = open(resultfile, 'w')
	for value in stus.values():
		result.write(str(value) + '\n')

def buildstrus(namesfile, scoresfile):
	stus = createstus(namesfile)
	return setscores(stus, scoresfile)

def createstus(namesfile):
	numandnames = open(namesfile)
	numandnameslines = numandnames.readlines()

	stus = {}
	for line in numandnameslines:
		sublines = line.split('\t')
		stu, stu.name = Stu(sublines[0]), sublines[1].replace('\n',"")
		stus[sublines[0]] = stu	

	return stus

def setscores(stus, scoresfile):
	numscores = open(scoresfile)
	numscorelines = numscores.readlines()

	for line in numscorelines:
		sublines = line.split('\t')
		try:
			stus[sublines[0]].setScore(sublines[1].replace('\n',""))
		except Exception as e:
			print(sublines[0])

	return stus

if __name__ == "__main__":
	resultfile = 'result.txt'
	namesfile = 'names.txt'
	scoresfile = 'scores.txt'
	writescores(buildstrus(namesfile, scoresfile), resultfile)
