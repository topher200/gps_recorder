#!/usr/bin/python2.6
from __future__ import with_statement
import android
import configobj
import json
import time

def record():
  # Figure out our output filename
  config_file = configobj.ConfigObj(config_filename)
  file_num = config_file['last_id'] + 1
  config_file['last_id'] = file_num
  output_filename = 'gps_output_{0}.json'.format(file_num)

  # Start location messages
  droid = android.Android()
  droid.startLocating(0, 0)
  droid.makeToast("Starting location drill")

  # Show a dialog box
  droid.dialogCreateAlert("GPS Recorder running")
  droid.dialogSetNeutralButtonText("Exit")
  droid.dialogShow()

  # Loop until the user exits
  with open(output_filename, 'w') as out_file:
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

    # Shutdown
    droid.stopLocating()
    droid.makeToast("Recording done, saving")

  droid.makeToast("All done - exiting!")

if __name__ == '__main__':
  record()
