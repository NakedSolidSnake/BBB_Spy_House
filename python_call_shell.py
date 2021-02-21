import subprocess


def capture():
  photo_state = subprocess.call(['./takephoto.sh'])
  print photo_state
  return photo_state

def remove():
  photo_state = subprocess.call(['./removephoto.sh'])
  return photo_state
