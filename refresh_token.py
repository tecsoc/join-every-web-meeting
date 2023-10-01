import binascii
import os

import dotenv

if __name__ == '__main__':
  dotenv_file = dotenv.find_dotenv()
  secret = binascii.hexlify(os.urandom(24)).decode('utf-8')
  dotenv.set_key(dotenv_file, 'secret', secret)
  print(secret)