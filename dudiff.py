#!/usr/bin/env python

import re
import sys


def warning(message):
	sys.stderr.write(message + '\n')


def load_du_log(fname):
	res = {}
	#with open(fname) as f:
	#	for line in f:
	#		line = line.strip()
	#		if line:
	#			m = re.match('^([0-9]+)\\s+(.*)$', line)
	#			if m:
	#				res[m.group(2)] = int(m.group(1))
	#			else:
	#				warning('Ignore invalid line: ' + line);
	f = open(fname)
	for line in f:
		line = line.strip()
		if line:
			m = re.match('^([0-9]+)\\s+(.*)$', line)
			if m:
				res[m.group(2)] = int(m.group(1))
			else:
				warning('Ignore invalid line: ' + line);
	f.close()
	
	return res;


def print_log(ls, title):
	print(title + ":")
	for item in sorted(ls, key=lambda tup: -tup[1]):
		print('\t' + ('%12d' % item[1] + ' ' + item[0]))
		
		
if len(sys.argv) != 3:
	warning("Usage: " + sys.argv[0] + " old_du_output new_du_output ")
	exit()
	
list_o = load_du_log(sys.argv[1])
list_n = load_du_log(sys.argv[2])

log = {
	'deleted': [],
	'new': [],
	'reduced': [],
	'growed': [],
}

for d, so in list_o.iteritems():
	if d not in list_n:
		log['deleted'].append((d, so))
	else:
		sn = list_n[d]
		if sn > so:
			log['growed'].append((d, sn - so))
		elif sn < so:
			log['reduced'].append((d, so - sn))

for d, sn in list_n.iteritems():
	if d not in list_o:
		log['new'].append((d, sn))

for title, ls in log.iteritems():
	print_log(ls, title)