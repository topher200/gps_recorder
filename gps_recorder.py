#!/usr/bin/python2.6
import android
import pickle
import time

def record():
  droid = android.Android()
  droid.startLocating(0, 0)
  # TODO(topher): will need this when not debugging
  # time.sleep(1)
  droid.makeToast("Starting location drill")
  results = []
  for _ in range(1000):
    res = droid.eventWaitFor(u'location', 1000)
    try:
      loc = res.result['gps']
    except KeyError:
      print("Error: no gps found")
      continue
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
