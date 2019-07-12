# -*- coding:utf-8 -*-
from lxml import etree
#from collections import Iterable
# https://blog.csdn.net/ydw_ydw/article/details/82227699

def decode(items):
	for item in items:
		if isinstance(item, etree._Element):
			decode(item)
	#if items.text != None and items.text.strip() != '':
	print("tag = %s, text = %s, attr = %s" % (items.tag, items.text, items.attrib))


def main():
	text ='''<?xml version="1.0" encoding="utf-8"?>
		 <item tag='itemtag'>
			 <cuo>c</cuo>
			 <fv><subfv>sub</subfv></fv>
			 <data>
			 <CaseInfo>abc</CaseInfo>
			 </data>
		 </item>
		'''
	
	root = etree.fromstring(text.encode('utf-8')) #解析对象输出代码

	decode(root)

	"""
	print('root.text = %s' % root.text)
	print('root.tag = %s' % root[1].tag) 

	child = etree.SubElement(root, 'child')
	child.text = 'childtext'
	print(etree.tostring(root).decode('utf-8'))
	"""

if __name__ == '__main__':
	main()