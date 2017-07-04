#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'George Cui'

class Stu:
	def __init__(self, id):
		self.id = id
		self.score = '0'

	def setName(self, name):
		self.name = name

	def setScore(self, score):
		self.score = score

	def __str__(self):
		return self.id + ' ' + self.name + '   ' + self.score

def writescores(stus, resultfile):
	result = open(resultfile, 'w')
	for value in stus.values():
		result.write(str(value) + '\n')

def buildstrus(namesfile, scoresfile):
	stus = createstus(namesfile)
	return setscores(stus, scoresfile)

def createstus(namesfile):
	idandnames = open(namesfile)
	idndnameslines = idandnames.readlines()

	stus = {}
	for line in idndnameslines:
		sublines = line.split('\t')
		stu, stu.name = Stu(sublines[0]), sublines[1].replace('\n',"")
		stus[sublines[0]] = stu	

	return stus

def setscores(stus, scoresfile):
	idscores = open(scoresfile)
	idscorelines = idscores.readlines()

	for line in idscorelines:
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
