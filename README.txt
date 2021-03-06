# Android GPS Recorder

## Introduction
   The GPS Recorder is a small script that logs the current GPS location as
   frequently as possible. It uses Scripting Language for Android to run it in
   Python!


## Usage
   To run the recorder, start gps_recorder.py on the Android phone using
   SL4A. Instructions for this can be found on the SL4A site:
   http://code.google.com/p/android-scripting/wiki/RemoteControl

   After running the script, use get_output_files.sh to retrieve the logs from
   the phone.

   You can parse and plot the output using the utilty functions in
   data_viewer.py.

   You can also use the conv2gpx script to convert the recorded
   tracks to the commongly uses GPX (GPS Exchange) Format used by geotagging and
   tracking software such as Google Earth. The script will load all the gps
   recordings into one file, with one track per file, split into sub-tracks if no
   data was captured for a short period.

   To record the sensor data from the phone instead of GPS, use
   sensor_recorder.py. This is a direct copy/pasta from gps_recorder.py,
   written as a last minute hack to try to get high frequency data out of the
   phone. It should work fine. See the blog post for more info.

   To record the apparent bearing from the device, use bearing_recorder.py. This
   uses the accelerometer to determine which axis is vertical, and then works out
   the apparent magnetic bearing. This may not be accurate. Bearings are measured
   clockwise from the positive x-axis around the vertical axis, unless x is
   vertical, in which case the bearings are made from the positive z-axis.


## Changelog
  v1.00: Initial release!


## Blog post
  A short blog post about this project is available here:
  http://blog.tophernet.com/2011/07/python-scripting-to-access-android-gps.html

  The source for this project is available on Github:
  https://github.com/topher200/gps_recorder


## License
  Copyright Topher Brown <topher200@gmail.com>, 2011. Released under the MIT
  license.
