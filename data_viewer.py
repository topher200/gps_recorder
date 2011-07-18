#!/usr/bin/python2.6
from __future__ import with_statement
import json
import pylab
import util

def parse_input(fileid = util.get_last_fileid()):
  filename = util.OUTPUT_FILENAME_TEMPLATE.format(fileid)
  results = []
  with open(filename, 'r') as f:
    for line in f.readlines():
      if line[0] == '#':
        # this is a comment, skip
        continue
      results.append(json.loads(line))

  coords = [(res['latitude'], res['longitude']) for res in results]

  print "found {0} unique records out of {1} total records".format(
    len(set(coords)), len(coords))
  return coords

def plot(coords=None):
  if (coords == None):
    coords = parse_input()
  x = [x for x, _ in coords]
  y = [y for _, y in coords]
  pylab.plot(x, y, linewidth=1.0)
  pylab.show()

def plot_in_pieces(coords=None, num_steps = 5):
  if (coords == None):
    coords = parse_input()

  for i in range(1, num_steps+1):
    step = ((len(coords) / num_steps) * i)
    plot(coords[:step])
