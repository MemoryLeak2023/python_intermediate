import datetime as dt
def log_time(message, time=dt.datetime.now()):
  print("{0}: {1}".format(time.isoformat(), message))

log_time("Log message 1")
log_time("Log message 2")
log_time("Log message 3")