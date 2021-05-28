import time
def timer(limit_time, init_time, logout_fun):
  print('diff', int(time.time()) - init_time)
  if limit_time.time and int(time.time()) - init_time >= int(limit_time.time):
    print('You will be disconnected')
    logout_fun([])