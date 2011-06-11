#!/usr/bin/python2.6
import android
import pickle
import time

def record():
  droid = android.Android()
  droid.makeToast("Starting location drill")
  results = []
  for _ in range(100):
    time.sleep(.1)
    loc = droid.readLocation().result
    print(loc)
    results.append(loc)

  try:
    f = open('gps_output.txt', 'w')
    pickle.dump(results, f)
  finally:
    f.close()

  droid.makeToast("Done!")

if __name__ == '__main__':
  record()

def parse_input():
  try:
    f = open('gps_output.txt', 'r')
    results = pickle.load(f)
  finally:
    f.close()

  for res in results:
    print(res['latitude'] + ' ' + res['longitude'])

