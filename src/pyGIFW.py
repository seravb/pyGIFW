#!/usr/bin/python
# -*- coding: utf-8 -*-

# File: pyGIFW.py -> pyGetImagesFromWebsitesModule

# Copyright (c) 2011 Serafín Vélez Barrera

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
################################################################################
################################################################################
Is a module written in Python that this one get from a web page the html code
and find inside all sources of the images that contains.
################################################################################
################################################################################
Syntax:
	pyGIFWM option [params] [extensions]

option:
	0 -> Only get the images from 1 website.
		syntax: 	pyGIFWM 0 url [extensions]
		generate:	img_url_ext[1..n].sh
	1 -> Get images from a url template website.
		syntax:		pyGIFWM 1 urlT iniNum finNum [extensions]
		generate:	img_urlT[iniNum..finNum]_ext[1..n].sh
	2 -> Get images from the websites that are written in a file.
		syntax:		pyGIFWM 2 file.txt [extensions]
		generate:	img_url[1..n].sh
	3 -> To get the list of known extensions.
		syntax:		pyGIFWM 3
		generate:	STDOUT 'ext1' ..  'extN'
	4 -> To view the license of this  app
		syntax:		pyGIFWM 4
		generate:	STDOUT Module's License
params:
	The params must be one url, a template of one url with an initialNumber
	and with a finalNumber to add to the url template, and in last option
	of param it could be a file (filename) in which one there is a list
	of urls websites.

extensions:
	Is the list of extensions that the module get from the
	website(s), if is not given any extension, by default
	the module get all the images that he know. Each extension of
	this list must not have an initial dot, example:
		Incorrect: '.png'
		Correct:    'png'
################################################################################
Examples:
	pyGIFWM	0 http://www.fsf.org/ png jpg
	   "	1 http://www.fsf.org/ 1 150 png jpg
	   "	2 textfile.txt png jpg
	   "	3
	   "	4
################################################################################
"""
import urllib
import re
import sys
import os
################################################################################
extensions=['all', 'jpg', 'gif', 'png', 'bmp', 'ocr', 'jpeg']
################################################################################
def license():
	"""
	name:		license()
	brief:		Function that tells the license of this module.

	return:		Nothing
	"""
	os.system("clear") # Instruction that call the OS to clear the terminal
	print "\
	File: pyGIFWM.py -> pyGetImagesFromWebsitesModule\
	Copyright (c) 2011 Serafín Vélez Barrera\
	\
	This program is free software: you can redistribute it and/or modify\
	it under the terms of the GNU General Public License as published by\
	the Free Software Foundation, either version 3 of the License, or\
	(at your option) any later version.\
	\
	This program is distributed in the hope that it will be useful,\
	but WITHOUT ANY WARRANTY; without even the implied warranty of\
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\
	GNU General Public License for more details.\
	\
	You should have received a copy of the GNU General Public License\
	along with this program.  If not, see <http://www.gnu.org/licenses/>."
################################################################################
def getExtensions():
	"""
	name:		getExtensions()
	brief:		Get extensions like a string.

	return:		String with the known extensions.
	"""
	ext=''
	for i in range(1, len(extensions)):
		ext += str.upper(extensions[i]) + "\n"
	return ext
################################################################################
def getFormatedExtensions():
	"""
	name:		getFormatedExtensions()
	brief:		Get extensions formated like a menu in a string.

	return:		String with the known formated extensions.
	"""
	ext="1.- " + extensions[0] + " posible extensions\n"
	for i in range(1, len(extensions)):
		ext = ext + str((i+1)) + ".- " + extensions[i] + "\n"
	return ext
################################################################################
def getExtension(i):
	"""
	name:		getExtension()
	brief:		Get extension in the 'i' position.

	param 	i:
			Position of the extension to return.

	return:		Extension in the 'i' place.
	"""
	return extensions[i]
################################################################################
def removeInitialDot(extension):
	"""
	name: 		removeInitialDot()
	brief: 		Find the initial dot in the extension string and this is removed if it's in the string.

	param	extension:
			String that which one is the extension.

	return: 	Extension without the initial dot.
	"""
	if extension[0]=='.':
		return extension.lstrip('.')
	else:
		return extension
################################################################################
def swapSymbolBySlash(url):
	"""
	name:		swapSymbolBySlash
	brief: 		Swap all the symbols like '.', '/', etc with a '_'

	param	url:
			String with an url.

	return:		Modified url.
	"""
	symbols=['/', '-', ':', '.', '·', ';', ',', '¿', '?',  '&',  '¡', '!', \
	'$', '%', '(', ')', '=', '|', '@', '#', '¬', '{', '}', '[', ']', '+', \
	'*', '<', '>']
	url = url.replace('http://', '')
	url = url.replace('www.', '')
	for i in symbols:
		url = url.replace(i, '_')
	return url
################################################################################
def getImgFromUrl(urlSource, extension):
	"""
	name: 		getImgFromUrl
	brief:		Get images from a url template.

	param 	urlSource:
			Url from where get the links of the images.
	param 	extension:
			Extension to add the regular expression.

	return: 	All the links that match with the regular expresion.
	"""
	# GET HTML
	url = urllib.urlopen(urlSource)
	html = url.read()
	# REGULAR EXPRESION COMPILATION
	expresion = r'<img src="([^"]+).' + extension + '"'
	regexp = re.compile(expresion, re.I | re.MULTILINE | re.DOTALL)
	# FIND ALL CASES OF THE REG. EXPR.
	links = regexp.findall(html)
	# CREATING A LIST WITH ALL THE LINKS THAT MATCH WITH THE REG. EXPR.
	i=0
	while i<len(links):
		links[i]=links[i]+'.'+extension
		print links[i], "\n"
		i += 1

	return links
################################################################################
def writeFileWithLinks(filename, urlSource, links):
	"""
	name: 		writeFileWithLinks()
	brief: 		Write a file with name equal to 'filename' with the img links.

	param 	filename:
			File with name 'filename' to write.
	param 	urlSource:
			url of the website.
	param 	links:
			links to download.

	return:		Nothing.
	"""
	f = file(filename, "wb+")
	try:
		line = "#!/bin/sh \nmkdir img_" + urlSource + "\ncd img_" + urlSource + "\n"
		f.write(line)
		for i in links:
			line = "wget " + i + "\n"
			f.write(line)
	finally:
		f.close()
################################################################################
def getUrlFromFile(filename):
	"""
	name: 		getUrlFromFile()
	brief: 		Read a file and gets all the links.

	param 	filename:
			Is the name of a file that which one contain a list of urls.

	return:		Nothing
	"""
	try:
		f = open(filename, 'r')
		urls=[]
	except:
		return urls
	finally:
		for i in f:
			urls.append(i)
		try:
			f.close()
		except:
			return urls
		return urls
################################################################################
#	__main__
################################################################################
if __name__ == "__main__":
	nparam=len(sys.argv)
	option=-1
	try:
		option = int(sys.argv[1])
	except:
		print "You should run the module with an allowed option."
		print "Options: 0, 1, 2, 3, 4, 5. View the module's help for the details."

	if nparam>=3:
		if   option==0:	# Only get the images from 1 website
			print "ONLY 1 WEBSITE"
			url = sys.argv[2]
			if nparam>3:	# The module must read given extensions
				for i in range(3, nparam):
					extension = sys.argv[i]
					links = getImgFromUrl(url, extension)
					if len(links)!=0:
						filename="img_"+sys.argv[i]+".sh"
						url = swapSymbolBySlash(url)
						writeFileWithLinks(filename, url, links)
			else:		# The module must use all extensions
				for i in range(1, len(extensions)):
					extension = extensions[i]
					links = getImgFromUrl(url, extension)
					if len(links)!=0:
						filename="img_"+extensions[i]+".sh"
						url = swapSymbolBySlash(url)
						writeFileWithLinks(filename, url, links)
		elif option==1: # Get images from a url template website
			print "URL TEMPLATE"
			urlTemplate   = sys.argv[2]
			initialNumber = sys.argv[3]
			finalNumber   = sys.argv[4]
			while initialNumber <= finalNumber:
				url = urlTemplate + str(initialNumber) + '/'
				if nparam>5:	# The module must read given extensions
					for i in range(5, nparam):
						extension = sys.argv[i]
						links = getImgFromUrl(url, extension)
						if len(links)!=0:
							filename="img_"+sys.argv[i]+".sh"
							url = swapSymbolBySlash(url)
							writeFileWithLinks(filename, url, links)
				else:		# The module must use all extensions
					for i in range(1, len(extensions)):
						extension = extensions[i]
						links = getImgFromUrl(url, extension)
						if len(links)!=0:
							filename="img_"+extensions[i]+".sh"
							url = swapSymbolBySlash(url)
							writeFileWithLinks(filename, url, links)
				initialNumber+=1
		elif option==2: # Get images from the websites inside of a file
			print "READ A FILE"
			urls = getUrlFromFile(sys.argv[2])
			if len(urls)>0:
				for url in urls:
					url=str.strip(url, '\n')
					if nparam>3:	# The module must read given extensions
						for i in range(3, nparam):
							extension = sys.argv[i]
							links = getImgFromUrl(url, extension)
							if len(links)!=0:
								filename="img_"+sys.argv[i]+".sh"
								url = swapSymbolBySlash(url)
								writeFileWithLinks(filename, url, links)
					else:		# The module must use all extensions
						for i in range(1, len(extensions)):
							extension = extensions[i]
							links = getImgFromUrl(url, extension)
							if len(links)!=0:
								filename="img_"+extensions[i]+".sh"
								url = swapSymbolBySlash(url)
								writeFileWithLinks(filename, url, links)
		else:
			print "Error in the given option"
	elif nparam == 2:
		if option==3: # To get all known extensions
			print "ALL KNOWN EXTENSIONS"
			for i in range(1, len(extensions)):
				print str.upper(extensions[i])
		elif option==4: # To view the module's license
			license()
		else:
	else:		# Error in the syntax
		print "Error in the syntax command or in the given option"
