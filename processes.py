#!/usr/bin/python3

import sys
import os

for line in os.popen("pslist"):
  linewords = line.split(" ")
  print(linewords[1])
