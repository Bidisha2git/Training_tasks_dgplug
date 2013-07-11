#!/usr/bin/env python
open('/proc/mounts')
print f.read()
f.close()
