#!/usr/bin/python2.6
import pickle
import pylab

def parse_input():
  try:
    f = open('gps_output.txt', 'r')
    results = pickle.load(f)
  finally:
    f.close()

  coords = []
  for res in results:
    coords.append((res['latitude'], res['longitude']))

  print "found {0} unique records".format((len(set(coords))))
  return coords

def plot(coords):
  x = [x for x, _ in coords]
  y = [y for _, y in coords]
  pylab.plot(x, y, linewidth=1.0)
  pylab.show()
