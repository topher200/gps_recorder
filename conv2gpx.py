import os
from xml.dom import getDOMImplementation
import json
import time
import re

impl = getDOMImplementation()
doc = impl.createDocument(None,'gpx',None)
top_element = doc.documentElement
top_element.setAttribute('version','1.0')
top_element.setAttribute('creator','Android GPS Tracker')
top_element.setAttribute('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance')
top_element.setAttribute('xmlns','http://www.topografix.com/GPX/1/0')
top_element.setAttribute('xsi:schemaLocation','http://www.topografix.com/GPX/1/0 http://www.topografix.com/GPX/1/0/gpx.xsd')

OUTPUT_FILENAME_TEMPLATE = 'gps_output_{0}.json'

for filename in os.listdir(os.getcwd()):
  match = re.match(OUTPUT_FILENAME_TEMPLATE.format('(\d*)'), filename)
  try:
    id = int(match.group(1))
  except AttributeError:
    continue
  track = doc.createElement('trk')
  track.appendChild(doc.createElement('name')).appendChild(doc.createTextNode('Track {0}'.format(id)))
  trackseg = doc.createElement('trkseg')
  lasttime = 0
  f = open(filename,'r')
  for line in f:
    try:
      point = json.loads(line)
      if ((int(point['time'])-lasttime) > 1000) and trackseg.hasChildNodes():
        track.appendChild(trackseg)
        trackseg = doc.createElement('trkseg')
      lasttime = int(point['time'])
      trackpoint = doc.createElement('trkpt')
      trackpoint.setAttribute('latitude',str(point['latitude']))
      trackpoint.setAttribute('longitude',str(point['longitude']))
      trackpoint.appendChild(doc.createElement('time')).appendChild(doc.createTextNode(str(time.strftime('%Y-%m-%dT%H-%M-%S',time.gmtime(float(point['time'])/1000)))))
      trackpoint.appendChild(doc.createElement('ele')).appendChild(doc.createTextNode(str(point['altitude'])))
      trackpoint.appendChild(doc.createElement('speed')).appendChild(doc.createTextNode(str(point['speed'])))
      trackpoint.appendChild(doc.createElement('pdop')).appendChild(doc.createTextNode(str(point['accuracy'])))
      trackpoint.appendChild(doc.createElement('fix')).appendChild(doc.createTextNode('3d'))
      trackseg.appendChild(trackpoint)
    except ValueError:
      print 'Invalid JSON: ' + line
      continue
  f.close()
  track.appendChild(trackseg)
  top_element.appendChild(track)

f = open('gpstrack.gpx','w+')
f.write(doc.toxml())
f.close
