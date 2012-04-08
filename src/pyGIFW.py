#!/usr/bin/python
# -*- coding: utf-8 -*-

# File: pyGIFW.py -> pyGetImagesFromWebsites

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
DESCRIPTION:
	Is a module written in Python that this one get from a web page the html
	code and find inside all sources of the images that contains.
################################################################################
################################################################################
NOTE:
	The program is not responsible for the licensing of images.
################################################################################
################################################################################
Syntax:
	pyGIFWM option [params] [extensions]

option:
	0 -> Only get the images from 1 website.
		syntax: 	pyGIFW 0 url [extensions]
		generate:	img_url_ext[1..n].sh
	1 -> Get images from a url template website.
		syntax:		pyGIFW 1 urlT iniNum finNum [extensions]
		generate:	img_urlT[iniNum..finNum]_ext[1..n].sh
	2 -> Get images from the websites that are written in a file.
		syntax:		pyGIFW 2 file.txt [extensions]
		generate:	img_url[1..n].sh
	3 -> To get the list of known extensions.
		syntax:		pyGIFW 3
		generate:	STDOUT 'ext1' ..  'extN'
	4 -> To view the license of this  app
		syntax:		pyGIFW 4
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
################################################################################
extensions=['all', 'jpg', 'gif', 'png', 'bmp', 'ocr', 'jpeg']
################################################################################
def license():
	"""
	name:		license()
	brief:		Function that displays the license of this module.

	return:		Nothing
	"""
	os.system("clear") # Instruction that call the OS to clear the terminal
	print "\
	File: pyGIFWM.py -> pyGetImagesFromWebsitesModule \n\
	Copyright (c) 2011 Serafín Vélez Barrera \n\
	\n\
	This program is free software: you can redistribute it and/or modify \n\
	it under the terms of the GNU General Public License as published by \n\
	the Free Software Foundation, either version 3 of the License, or \n\
	(at your option) any later version. \n\
	\n\
	This program is distributed in the hope that it will be useful, \n\
	but WITHOUT ANY WARRANTY; without even the implied warranty of \n\
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the \n\
	GNU General Public License for more details. \n\
	\n\
	You should have received a copy of the GNU General Public License \n\
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
	brief: 		Write a file with name equal to 'filename' with the img
				links.

	param 	filename:
			File with name 'filename' to write.
	param 	urlSource:
			Url of the website.
	param 	links:
			Links to download.

	return:		Nothing.
	"""
	f = file(filename, "wb+")
	try:
		line = "#!/bin/sh \nmkdir img_" + urlSource + "\ncd img_" + \
			urlSource + "\n"
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
			Is the name of a file that which one contain a list of
				urls.

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
def createFileWithLinks(links, url, extension):
	"""
	name: 		createFileWithLinks()
	brief: 		If there is links to save create the file to save them.

	param 	links:
			Is the name of a file that which one contain a list of
				urls.
	param	url:
			Url of the website.
	param	extension:
			Extension of the images to download.

	return:		Nothing
	"""
	if len(links)!=0:
		filename="img_"+extension+".sh"
		writeFileWithLinks(filename, url, links)
################################################################################
#	__main__
################################################################################
if __name__ == "__main__":
	nparam=len(sys.argv)
	option = int(sys.argv[1])
	if nparam>=3:
		if   option==0:	# Only get the images from 1 website
			url = sys.argv[2]
			if nparam>3:	# The module must read given extensions
				for i in range(3, nparam):
					print "Images in ", sys.argv[i]
					links = getImgFromUrl(url, sys.argv[i])
					createFileWithLinks(links, url, sys.argv[i])
			else:		# The module must use all extensions
				for i in range(1, len(extensions)):
					print "Images in ", extensions[i]
					links = getImgFromUrl(url, extensions[i])
					createFileWithLinks(links, url, extensions[i])
		elif option==1: # Get images from a url template website
			urlTemplate = sys.argv[2]
			initialNumber = sys.argv[3]
			finalNumber   = sys.argv[4]
			while initialNumber < finalNumber:
				url = urlTemplate + str(initialNumber) + '/'
				if nparam>5:	# The module must read given extensions
					for i in range(3, nparam):
						print "Images in ", sys.argv[i]
						links = getImgFromUrl(url, sys.argv[i])
						createFileWithLinks(links, url, sys.argv[i])
				else:		# The module must use all extensions
					for i in range(1, len(extensions)):
						print "Images in ", extensions[i]
						links = getImgFromUrl(url, extensions[i])
						createFileWithLinks(links, url, extensions[i])
		elif option==2: # Get images from the websites inside of a file
			urls = getUrlFromFile(sys.argv[2])
			if len(urls)>0:
				for url in urls:
					# If the last character is a \n, this is
					# removed to create a good url for the
					# download
					if url[len(url)-1]=='\n':
						url=str.strip(url, '\n')
					if nparam>3:	# The module must read given extensions
						for i in range(3, nparam):
							print "Images in ", sys.argv[i]
							links=getImgFromUrl(url, sys.argv[i])
							createFileWithLinks(links, url, sys.argv[i])
					else:		# The module must use all extensions
						for i in range(1, len(extensions)):
							print "Images in ", extensions[i]
							links=getImgFromUrl(url, extensions[i])
							createFileWithLinks(links, url, extensions[i])
		else:
			print "Error in the given option"
	elif nparam == 2:
		if option==3: # To get all known extensions
			print "ALL KNOWN EXTENSIONS"
			for i in range(1, len(extensions)):
				print str.upper(extensions[i])
		elif option==4: # To view the module's license
			license()
		#else:
	else:		# Error in the syntax
		print "Error in the syntax command or in the given option"
		print "Syntax: python pyGIFW option <extension(s)>"
