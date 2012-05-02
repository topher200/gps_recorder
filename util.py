#!/usr/bin/python2.6
import os
import re

def get_last_fileid():
  last_id = 0
  for filename in os.listdir(os.getcwd()):
    match = re.match(OUTPUT_FILENAME_TEMPLATE.format('(\d*)'), filename)
    try:
      id = int(match.group(1))
    except AttributeError:
      continue
    if last_id < id:
      last_id = id
  return last_id

