This is the solution for the code mount.py. In this code we write a function to open the file name /proc/mounts/. The contents of the file is the required output.

This code gives the required output:

#!/usr/bin/env python
f = open('/proc/mounts')
print f.read()
f.close()

The link to the soultion is:


