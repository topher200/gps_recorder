#!/usr/bin/python2.6
from __future__ import with_statement
from util import get_last_fileid
import android
import json

OUTPUT_FILENAME_TEMPLATE = 'gps_output_{0}.json'

def record():
  # Start location messages
  droid = android.Android()
  droid.startLocating(0, 0)
  droid.makeToast("Starting location drill")

  # Show a dialog box
  droid.dialogCreateInput("GPS Recorder running", "Add message to log")
  droid.dialogSetPositiveButtonText("Log message")
  droid.dialogSetNegativeButtonText("Exit")
  droid.dialogShow()

  # Loop until the user exits
  out_filename = OUTPUT_FILENAME_TEMPLATE.format(get_last_fileid() + 1)
  with open(out_filename, 'w') as out_file:
    running = True
    while running:
      # Wait until we get an event
      res = droid.eventWait(1000).result
      if res == None:
        print "LocationListener timeout"
      elif res['name'] == "dialog":
        # User used the dialog
        if (res[u'data'][u'which'] == u'positive'):
          droid.makeToast("Saving log message")
          message = '# {0}'.format(res[u'data'][u'value'])
          print message
          out_file.write('{0}\n'.format(message))
          droid.dialogShow()
        else:
          print "User requested exit"
          running = False
      elif res['name'] == "location":
        # It's a GPS message!
        try:
          loc = res['data']['gps']
        except (KeyError, TypeError):
          print("Location message, but no GPS data")
          continue
        print(loc)
        out_file.write(json.dumps(loc) + '\n')

    # Shutdown
    droid.stopLocating()

  droid.makeToast("All done - saved to {0}".format(out_filename))

if __name__ == '__main__':
  record()
