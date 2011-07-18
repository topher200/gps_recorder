#!/usr/bin/python2.6
from __future__ import with_statement
from util import OUTPUT_FILENAME_TEMPLATE, get_last_fileid
import android
import json
import time

def record():
  # Start location messages
  droid = android.Android()
  droid.startSensingTimed(1, 50)
  droid.makeToast("Starting sensing")

  # Show a dialog box
  droid.dialogCreateInput("Sensor Recorder running", "Add message to log")
  droid.dialogSetPositiveButtonText("Log message")
  droid.dialogSetNegativeButtonText("Exit")
  droid.dialogShow()

  # Loop until the user exits
  out_filename = OUTPUT_FILENAME_TEMPLATE.format(get_last_fileid() + 1)
  with open(out_filename, 'w') as out_file:
    running = True
    time.sleep(10)
    while running:
      res = droid.eventWait(1000).result
      print res
      if res == None:
        print "LocationListener timeout"
      elif res['name'] == "dialog":
        # User saving a comment
        if (res[u'data'][u'which'] == u'positive'):
          droid.makeToast("Saving log message")
          message = '# {0}'.format(res[u'data'][u'value'])
          print message
          out_file.write('{0}\n'.format(message))
          droid.dialogShow()
        else:
          print "User requested exit"
          running = False
      elif res['name'] == "sensors":
        # We've got what we're looking for!
        print(res)
        out_file.write(json.dumps(res) + '\n')

    # Shutdown
    droid.stopLocating()

  droid.makeToast("All done - saved to {0}".format(out_filename))

if __name__ == '__main__':
  record()
