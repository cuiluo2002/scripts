#!/usr/bin/python
# -*- coding: UTF-8 –*-

__author__ = 'George Cui'

import scipy.io

def readmat():
	data = scipy.io.loadmat('../MatlabCodes/data_dis_sym_ref.mat')
	#print (data.keys())
	#w = data['W']
	#print(w[7][6])

	#sdat = data['Sdat']
	#print(sdat[0][0])

	dis = data['Dis']
	print(dis[0][0])


if __name__=="__main__":
	readmat()