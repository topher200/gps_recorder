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

  for i in range(num_steps):
    step = ((len(coords) / num_steps) * i)
    plot(coords[:step])
