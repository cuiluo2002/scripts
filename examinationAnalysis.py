#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'George Cui'

excellent = 0
good = 0
moderate = 0
passmark = 0
fail = 0

total = 0

excellentpercentage = 0.0
goodpercentage = 0.0
moderatepercentage = 0.0
passmarkpercentage = 0.0
failpercentage = 0.0

def analyse(sourceDataFile):
	sourceData = open(sourceDataFile)
	sourceDataLines = sourceData.readlines()

	global total
	total = len(sourceDataLines)

	for line in sourceDataLines:
		score =  int(line)
		doAnalyse(score)

	calculatePercentage()

def doAnalyse(score):
	global excellent
	global good
	global moderate
	global passmark
	global fail

	if score >= 90:
		excellent = excellent + 1
	if score < 90 and score >= 80:
		good = good + 1
	if score < 80 and score >= 70:
		moderate = moderate + 1
	if score < 70 and score >= 60:
		passmark = passmark + 1
	if score < 60:
		fail = fail + 1

def calculatePercentage():
	global excellentpercentage
	global goodpercentage
	global moderatepercentage
	global passmarkpercentage
	global failpercentage

	excellentpercentage = doCalculate(excellent)
	goodpercentage = doCalculate(good)
	moderatepercentage = doCalculate(moderate)
	passmarkpercentage = doCalculate(passmark)
	failpercentage = doCalculate(fail)

def doCalculate(amount):
	global total
	return (float(amount) * 100) / total

if __name__=="__main__":
	sourceDataFile = '1.txt'
	analyse(sourceDataFile)

	print("excellent = %d, percentage = %.1f" % (excellent,excellentpercentage))
	print("good = %d, percentage = %.1f" % (good,goodpercentage))
	print("moderate = %d, percentage = %.1f" % (moderate,moderatepercentage))
	print("passmark = %d, percentage = %.1f" % (passmark,passmarkpercentage))
	print("fail = %d, percentage = %.1f" % (fail,failpercentage))