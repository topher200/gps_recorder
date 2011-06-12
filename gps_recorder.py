#!/usr/bin/python2.6
import android
import pickle
import time

def record(seconds = 10):
  droid = android.Android()
  droid.startLocating(0, 0)
  droid.makeToast("Starting location drill")
  droid.dialogCreateAlert("Exit?")
  droid.dialogSetNeutralButtonText("Exit")
  droid.dialogShow()
  results = []
  running = True
  while running:
    res = droid.eventWait(1000).result
    if res == None:
      print "LocationListener timeout"
      continue
    elif res['name'] == "dialog":
      # Dialog has been pressed- get out
      print "User requested exit"
      running = False
      continue
    elif res['name'] == "location":
      try:
        loc = res['data']['gps']
      except (KeyError, TypeError):
        print("Location message, but no GPS data")
        continue
    else:
      print "I have no idea what kind of message that was"
      print res
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
