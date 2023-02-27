> Write a Python program named catn.py by modifying the template code to implement the unix utility command cat with -n option, which adds the line number in front of every line of a file.

> First version: support the command with optional -n flag and one file.  Note that the line number is formatted 
```
$ python3 catn.py mary.txt
Mary had a little lamb
little lamb, little lamb
Mary had a little lamb
its fleece was white as snow
```
```
$ python3 catn.py -n mary.txt
     1  Mary had a little lamb
     2  little lamb, little lamb
     3  Mary had a little lamb
     4  its fleece was white as snow
```

> Second version: handles one or more files with optional -n flag.  In case of multiple files, the line number restarts from 1.