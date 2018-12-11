#!/usr/bin/python
# -*- coding: utf-8 -*-
# author Red liu
# monitor src files to do auto make

import os, time, sys

# get last modified time
# input a list of files
def get_last_mtime(files):
  mtime = 0.0

  if len(files) == 0:
    print("Can't get mtime for %s" % files)
    sys.exit(0)

  for i in files:
    suffix = os.path.splitext(i)[1]
    if mtime < os.path.getmtime(i):
      mtime = os.path.getmtime(i)
  return mtime

if __name__ == '__main__':
  if len(os.sys.argv) < 2:
    print "Usage: monitor.py xxx.rst or *.rst"
    exit()
  
  mtime = 0.0

  while True:
    last_mtime = get_last_mtime(os.sys.argv[1:])
    if mtime != last_mtime:
      print("-" * 30)
      os.system("make html")
      mtime = last_mtime
    
    time.sleep(3)
