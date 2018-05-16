import time

def pause(sec):
  def decorator(func):
    def wrapper(*args, **kwargs):
      time.sleep(sec)
      result = func(*args, **kwargs)
      return result
    return wrapper
  return decorator