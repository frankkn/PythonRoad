#!/usr/bin/env python3
a = '%c' % 65
print(a) # A

b = oct(65)
print(b) # 0o101

c = '\101' # octal: \ followed by 3 octal digits for ASCII
print(c) # A

d = hex(65)
print(d) # 0x41

e = '\x41' # hex: \x followed by 2 hex digits for ASCII
print(e) # A