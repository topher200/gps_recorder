#!/usr/bin/python2.6
from __future__ import with_statement
import android
import json
import os
import re

def determine_filename():
  # Add 1 to the last matching filename we can find.
  template = 'gps_output_{0}.json'
  last_id = 0
  for filename in os.listdir(os.getcwd()):
    match = re.match(template.format('(\d)'), filename)
    try:
      last_id = int(match.group(1))
    except AttributeError:
      pass
  return template.format(last_id + 1)

def record():
  # Start location messages
  droid = android.Android()
  droid.startLocating(0, 0)
  droid.makeToast("Starting location drill")

  # Show a dialog box
  droid.dialogCreateInput("GPS Recorder running")
  droid.dialogSetPositiveButtonText("Log message")
  droid.dialogSetNegativeButtonText("Exit")
  droid.dialogShow()

  # Loop until the user exits
  with open(determine_filename(), 'w') as out_file:
    running = True
    while running:
      res = droid.eventWait(1000).result
      if res == None:
        print "LocationListener timeout"
      elif res['name'] == "dialog":
        print "Dialog pressed"
        if (res[u'data'][u'which'] == u'positive'):
          # log the message
          message = '# {0}'.format(res[u'data'][u'value'])
          print message
          out_file.write(message)
        else:
          print "User requested exit"
          running = False
      elif res['name'] == "location":
        try:
          loc = res['data']['gps']
        except (KeyError, TypeError):
          print("Location message, but no GPS data")
          continue
        print(loc)
        out_file.write(json.dumps(loc) + '\n')

    # Shutdown
    droid.stopLocating()
    droid.makeToast("Recording done, saving")

  droid.makeToast("All done - exiting!")

if __name__ == '__main__':
  record()
