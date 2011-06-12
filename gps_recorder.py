#!/usr/bin/python2.6
from __future__ import with_statement
import android
import json
import time

def record():
  droid = android.Android()
  droid.startLocating(0, 0)
  droid.makeToast("Starting location drill")
  droid.dialogCreateAlert("GPS Recorder running")
  droid.dialogSetNeutralButtonText("Exit")
  droid.dialogShow()
  with open('gps_output.txt', 'w') as out_file:
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
      out_file.write(json.dumps(loc) + '\n')
    droid.stopLocating()
    droid.makeToast("Recording done, saving")

  droid.makeToast("All done - exiting!")

if __name__ == '__main__':
  record()
