 #!/usr/bin/env python

import base64
file1 = open("pwd.list", "r")
file2 = open("b64pwds.lst","w")

for line in file1:
    clear = "administrator:" + str.strip(line)
    new = base64.encodestring(clear)
    file2.write(new)