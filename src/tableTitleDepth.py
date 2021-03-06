# -*- coding: utf-8 -*-
'''
@author mjbommar
@date Jan 30, 2009
'''

import csv
import codecs
import cPickle
import glob
import htmlentitydefs
import igraph
import lxml.etree
import multiprocessing
import os.path
import pylab
import re
import sys
import zipfile

def initOutput():
	'''
	Setup the UTF-8 output.
	'''
	streamWriter = codecs.lookup('utf-8')[-1]
	sys.stdout = streamWriter(sys.stdout)

def loadTitle(titleN, elements):
	nodes = set()
	edges = set()
	
	titleString = 'TITLE {0} -'.format(titleN)
	titleAppendixString = 'TITLE {0} - APPENDIX'.format(titleN)
	
	depthDistribution = [e.count('_') for e in elements if e.startswith(titleString) and not e.startswith(titleAppendixString)]
	
	return depthDistribution

if __name__ == "__main__":
	initOutput()	
	
	elements = cPickle.load(open('data/elements.pickle'))
	titles = range(1,51)
	titles.remove(34)
	
	output_rows = []
	for t in titles:
		d = loadTitle(t, elements)
		row = [t, pylab.mean(d), pylab.std(d)]
		output_rows.append(row)
		print " & ".join(map(str,row)) + '\\\\\hline'

	
	output_file = csv.writer(open('results/table_title_depth.csv', 'w'))
	output_file.writerows(output_rows)
	
	
