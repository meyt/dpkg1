#!/usr/bin/python
# -*- coding: utf-8 -*-
# DPKG1 , Collect debian packages with all dependencies
# Author: Mahdi Ghane.G

import os, sys, apt, argparse, platform
try:
	#~~~ Define global vars
	THIS_PATH = os.path.dirname(os.path.abspath(__file__))
	OUTPUT_PATH = os.path.join(THIS_PATH,'pkgs')
	APT_CACHE = apt.Cache()
	APT_PKG = None
	PKG_NAME = None
	PKG_ARCH = None
	PKG_PATH = None
	PKG_DIST = None
	DEPENDS = []
	
	
	
	#~~~ Make output folder
	if not os.path.exists(OUTPUT_PATH):
		os.makedirs(OUTPUT_PATH)



	#~~~ Define options
	parser = argparse.ArgumentParser()
	parser.add_argument('-c', help='Collect packages', nargs='*')
	parser.add_argument('-i', help='Install packages', nargs='*')
	args = parser.parse_args()
	
	
	
	

	#~~~ Install packages
	if not args.i==None:
		
		for directory in os.listdir(OUTPUT_PATH):
			try:
				PKG_NAME, PKG_DIST, PKG_ARCH = directory.split('_')
			
				if PKG_NAME in args.i:
					PKG_PATH = os.path.join(OUTPUT_PATH, PKG_NAME+"_"+PKG_DIST+"_"+PKG_ARCH)
					os.chdir(PKG_PATH)
					os.system("dpkg -i -E -G *.deb")
			except:
				print 'ERROR:: Invalid directory name: '+directory
			
		







	#~~~ Collect packages
	if not args.c==None:
		PKG_DIST = platform.dist()[0]
		for PKG_NAME in args.c:
			### Check if package exits
			if PKG_NAME in APT_CACHE:
				APT_PKG = APT_CACHE[PKG_NAME]
				PKG_ARCH = APT_PKG.architecture()
				PKG_PATH = os.path.join(OUTPUT_PATH, PKG_NAME+"_"+PKG_DIST+"_"+PKG_ARCH)
				if not os.path.exists(PKG_PATH):
	    				os.makedirs(PKG_PATH)
				os.chdir(PKG_PATH)
	
			
				for item in APT_PKG.candidate.dependencies:
					for x in item:
						DEPENDS.append(x.name)
						os.system("fakeroot -u dpkg-repack "+x.name)
			
	
			
			
			else:
				print 'ERROR:: `%s` Not installed' %  PKG_NAME


	
except KeyboardInterrupt:
    print 'Force exit, Keyboard interrupt!'

