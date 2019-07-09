# -*- coding:utf-8 -*-
from lxml import etree
# https://blog.csdn.net/ydw_ydw/article/details/82227699
def main():
	text ='''<?xml version="1.0" encoding="utf-8"?>
		 <item tag='itemtag'>
			 <cuo></cuo>
			 <fv><subfv></subfv></fv>
			 <data>
			 <CaseInfo></CaseInfo>
			 </data>
		 </item>
		'''
	
	root = etree.fromstring(text.encode('utf-8')) #解析对象输出代码

	print(etree.tostring(root).decode('utf-8'))
	print('root.text = %s' % root.text)
	print('root.tag = %s' % root[1].tag) 

	child = etree.SubElement(root, 'child')
	child.text = 'childtext'
	print(etree.tostring(root).decode('utf-8'))


if __name__ == '__main__':
	main()