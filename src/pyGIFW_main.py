#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
File: pyGIFWMM_main.py -> pyGetImgFromWebsitesModule


Description: Is a script written in Python that this one get from a web page the html code and
find inside all sources of the images that contains.


Syntax:
	pyGIFWM 0 url [extensions]
	   "   1 urlT initialNumber finalNumber [extensions]
	   "   2 filename

Params:
	option:
		0 -> Only get the images from 1 website
		1 -> Get images from a url template website
		2 -> Get images from the websites that they are in a file [filename] with the following structure
			File ->	filename:
				x extension1 extension2 extensionN
				url1
				url2
				urlN
	[extension1, extensionN]:
		extension or extension's list of the images, if not given this param or list by default
			the script take the images with the '.jpg' extension.
		if extension1 is 'all' the script get all the images that he knows.
"""
from pyGIFWM import *

#extensions=['all', '.jpg', '.gif', '.png', '.bmp', '.ocr']


msgMenu="\
MENU \n\
0.- Quit \n\
1.- Get images from 1 url \n\
2.- Get images from a url template \n\
3.- Get images from the urls that are in a file \n\
Please, choose option: "

msgExtension='\
1.- All known extensions \n\
2.- JPG extension \n\
3.- GIF extension \n\
4.- PNG extension \n\
5.- BMP extension \n\
6.- OCR extension \n\
Please, choose option: '

msgError="Error in the selection, please choose again."

#########################################################################
#########################################################################
#				PROGRAM					#
#
print getExtensions()
option=1
optionExtension=-1

while option!=0:
	option=1
	while option>0 and option<3:
		try:
			option=int(raw_input(msgMenu))
		except:
			print msgError
		if option==0:
			print "Goodbye!"
		elif option == 1:
			url = raw_input('Write the url, please: ')
			url = "http://localhost/"
			while optionExtension<1 or optionExtension>7:
				try:
					optionExtension = int(raw_input(getExtensions()))
				except:
					print "Error in the selection, please choose again."

			if optionExtension == 1:	# all extension
				for i in range(1,len(extensions)):
					links=getImgFromUrl(url,extensions[i])
					filename=raw_input('Name of the output file (all extensions): ')
					writeFileWithLinks(filename+str(i)+extensions[i]+'.sh',url,links)
			elif optionExtension == 2:	# .jpg extension
				links=getImgFromUrl(url,extensions[1])
				filename=raw_input('Name of the output file (' + extensions[1] + '): ')
				writeFileWithLinks(filename+'.sh',url,links)
			elif optionExtension == 3:	# .gif extension
				links=getImgFromUrl(url,extensions[2])
				filename=raw_input('Name of the output file (' + extensions[2] + '): ')
				writeFileWithLinks(filename+'.sh',url,links)
			elif optionExtension == 4:	# .png extension
				links=getImgFromUrl(url,extensions[3])
				filename=raw_input('Name of the output file (' + extensions[3] + '): ')
				writeFileWithLinks(filename+'.sh',url,links)
			elif optionExtension == 5:	# .bmp extension
				links=getImgFromUrl(url,extensions[4])
				filename=raw_input('Name of the output file (' + extensions[4] + '): ')
				writeFileWithLinks(filename+'.sh',url,links)
			elif optionExtension == 6:	# .ocr extension
				links=getImgFromUrl(url,extensions[5])
				filename=raw_input('Name of the output file (' + extensions[5] + '): ')
				writeFileWithLinks(filename+'.sh',url,links)
			elif optionExtension == 7:	# .jpeg extension
				links=getImgFromUrl(url,extensions[6])
				filename=raw_input('Name of the output file (' + extensions[6] + '): ')
				writeFileWithLinks(filename+'.sh',url,links)
			else:
				print "Error in the selection"
		elif option == 2:
			print "2"
		elif option == 3:
			print "3"
		else:
			print msgError
