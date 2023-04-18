def count_files(p = '.'):
  import os
  return 1 if not os.path.isdir(p) \
    else sum(map(count_files, os.listdir(p)))