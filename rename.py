import os
import sys
import re

dir = sys.argv[1]
req = re.compile(r'css@')

print dir
print os.sep

for root, dirs, files in os.walk(dir):
  for filename in files:
    if req.search(filename):
      new_name = re.sub(r'css@.*$', 'css', filename)
      print filename
      os.rename(root + os.sep + filename, root + os.sep + new_name)

