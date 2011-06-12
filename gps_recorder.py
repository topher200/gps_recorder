#!/usr/bin/python2.6
import android
import pickle
import time

def record(seconds = 10):
  droid = android.Android()
  droid.startLocating(0, 0)
  # TODO(topher): will need this when not debugging
  # time.sleep(1)
  droid.makeToast("Starting location drill")
  results = []
  start = time.time()
  while((time.time() - start) < seconds):
    res = droid.eventWait(1000)
    try:
      loc = res.result['data']['gps']
    except (KeyError, TypeError):
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
