#!/usr/bin/python2.6
from __future__ import with_statement
from util import get_last_fileid
import android
import json
import math

VERTICAL_THRESHOLD = 9.2
OUTPUT_FILENAME_TEMPLATE = 'bearing_output_{0}.json'

def record():
  # Start location messages
  droid = android.Android()
  droid.startSensingTimed(1, 1000)
  droid.makeToast("Starting Bearing drill")

  # Show a dialog box
  droid.dialogCreateInput("Bearing Recorder running", "Add message to log")
  droid.dialogSetPositiveButtonText("Log message")
  droid.dialogSetNegativeButtonText("Exit")
  droid.dialogShow()

  out_filename = OUTPUT_FILENAME_TEMPLATE.format(get_last_fileid() + 1)
  with open(out_filename, 'w') as out_file:
    running = True
    while running:
      # Wait until we get an event
      res = droid.eventWait(1000).result
      if res == None:
        print "SensorListener timeout"
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
      elif res['name'] == 'sensors':
        data = {}
        data['time'] = res['data']['time']
        xforce = float(res['data']['xforce'])
        yforce = float(res['data']['yforce'])
        zforce = float(res['data']['zforce'])
        xmag = float(res['data']['xMag'])
        ymag = float(res['data']['yMag'])
        zmag = float(res['data']['zMag'])
        if abs(xforce) > abs(yforce) and abs(xforce) > abs(zforce):
          if xforce > VERTICAL_THRESHOLD:
            angle = math.atan2(-(ymag),zmag)
            if angle < 0:
              angle = angle + (2 * math.pi)
            bearing = int(math.degrees(angle))
            data['bearing'] = bearing
          elif xforce < -(VERTICAL_THRESHOLD):
            angle = math.atan2(ymag,zmag)
            if angle < 0:
              angle = angle + (2 * math.pi)
            bearing = int(math.degrees(angle))
            data['bearing'] = bearing
          elif xforce > 0:
            data['bearing'] = None
          else:
            data['bearing'] = None
        elif abs(yforce) > abs(xforce) and abs(yforce) > abs(zforce):
          if yforce > VERTICAL_THRESHOLD:
            angle = math.atan2(-(zmag),xmag)
            if angle < 0:
              angle = angle + (2 * math.pi)
            bearing = int(math.degrees(angle))
            data['bearing'] = bearing
          elif yforce < -(VERTICAL_THRESHOLD):
            angle = math.atan2(zmag,xmag)
            if angle < 0:
              angle = angle + (2 * math.pi)
            data['bearing'] = int(math.degrees(angle))
          elif yforce > 0:
            data['bearing'] = None
          else:
            data['bearing'] = None
        elif abs(zforce) > abs(yforce) and abs(zforce) > abs(xforce):
          if zforce > VERTICAL_THRESHOLD:
            angle = math.atan2(ymag,xmag)
            if angle < 0:
              angle = angle + (2 * math.pi)
            data['bearing'] = int(math.degrees(angle))
          elif zforce < -(VERTICAL_THRESHOLD):
            angle = math.atan2(-(ymag),xmag)
            if angle < 0:
              angle = angle + (2 * math.pi)
            data['bearing'] = int(math.degrees(angle))
          elif zforce > 0:
            data['bearing'] = None
          else:
            data['bearing'] = None
        else:
            data['bearing'] = None
        print(data)
        out_file.write(json.dumps(data) + '\n')


    # Shutdown
  droid.stopSensing()


if __name__ == '__main__':
  record()
