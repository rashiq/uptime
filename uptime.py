import sys
import os
import json
import socket
from urlparse import urlparse


def run_check(services, down_actions, up_actions):

  for service, data in services.items():
    url = data.get('url')
    port = data.get('port')

    is_up = ping(url, port)
    actions = up_actions if is_up else down_actions

    for action in actions:
      action = action.replace("$SERVICE", service)
      os.system(action)


def ping(url, port):
  if not url: return False

  parsed = urlparse(url)
  if parsed.netloc:
    url = parsed.netloc
  else:
    try:
      socket.inet_aton(url)
    except socket.error:
      return False

  if not port:
    port = 443 if parsed.scheme == 'https' else 80

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    result = sock.connect_ex((url, port))
  except Exception as e:
    return False

  return result == 0


if __name__ == '__main__':
  config_path = os.path.join(os.path.dirname(__file__), "config.json")

  if not os.path.exists(config_path):
    sys.exit("You need to create a config.json file")

  try:
    config = json.loads(open(config_path, 'r').read())
  except Exception as e:
    sys.exit("config.json file is invalid")

  services = config.get('services')
  down_actions = config.get('down')
  up_actions = config.get('up')

  if not services or not (down_actions or up_actions):
    sys.exit("You need to specify services, and a down or up action")

  run_check(services, down_actions, up_actions)
