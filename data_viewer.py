#!/usr/bin/python2.6
import pickle

def parse_input():
  try:
    f = open('gps_output.txt', 'r')
    results = pickle.load(f)
  finally:
    f.close()

  coords = []
  for res in results:
    coords.append((res['latitude'], res['longitude']))
  return coords

