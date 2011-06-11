#!/usr/bin/python2.6
import android
import pickle
import time

def record():
  droid = android.Android()
  droid.startLocating()
  time.sleep(1)
  droid.makeToast("Starting location drill")
  results = []
  for _ in range(100):
    time.sleep(.1)
    loc = droid.readLocation().result['gps']
    print(loc)
    results.append(loc)
  droid.stopLocating()
  droid.makeToast("Recording done, saving")

  try:
    f = open('gps_output.txt', 'w')
    pickle.dump(results, f)
  finally:
    f.close()

  droid.makeToast("All done - exiting!")

if __name__ == '__main__':
  record()
