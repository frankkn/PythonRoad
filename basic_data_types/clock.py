import time

while True:
  t = time.localtime()
  print('\r%02d:%02d:%02d' % (t.tm_hour, t.tm_min, t.tm_sec), end = '') # \r:同一列最左邊
  time.sleep(1)

