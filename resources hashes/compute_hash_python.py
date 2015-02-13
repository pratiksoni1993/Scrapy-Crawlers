import base64
from Crypto.Hash import SHA256
import sys

f = open(sys.argv[1]).read()
h = SHA256.new()
h.update(f)
print base64.urlsafe_b64encode(h.digest())[0:-1]
