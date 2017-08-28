#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'George Cui'

import sys
import os

def getTargetRootDir():
	assert(len(sys.argv) in range(1, 3))
	if len(sys.argv) == 2:
		rootPath = sys.argv[1]
	else:
		rootPath = os.getcwd()
	return rootPath

def makeTargetDir(fileName):
	names = fileName.split('_')
	#print(names)
	assert(int(names[1]) >= 20160529 and len(names[1]) == 8)
	targetDir = os.path.join(getTargetRootDir(), names[1])
	if not os.path.exists(targetDir):
		os.makedirs(targetDir)
	return targetDir

def isPictureOrVideo(fileName):
	names = fileName.split('.')
	if names[-1] in ('jpg', 'mp4', 'avi'):
		return True
	return False

def copyFile(sourceFile, targetFile):
	 if not os.path.exists(targetFile):
	 	open(targetFile, "wb").write(open(sourceFile, "rb").read()) 
	 elif os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile)):
	 	open(os.path.join(targetDir, "2.jpg"), "wb").write(open(sourceFile, "rb").read()) 

if __name__=="__main__":
	files = os.listdir()
	for file in files:
		if isPictureOrVideo(file):
			try:
				targetDir = makeTargetDir(file)
			except Exception as e:
				print(e)
				continue
			else:
				pass
			finally:
				pass
			
			copyFile(file, os.path.join(targetDir, file))