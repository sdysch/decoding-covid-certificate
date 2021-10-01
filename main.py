import zlib
import pprint

import PIL.Image
import pyzbar.pyzbar
import base45
import cbor2

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", metavar = "IMAGE", type = str, required = True)
args = parser.parse_args()

data = pyzbar.pyzbar.decode(PIL.Image.open(args.image))
#print(data)
cert = data[0].data.decode()

# removes HC1:
b45data = cert.lstrip("HC1:")

# decompress?
zlibdata = base45.b45decode(b45data)
cbordata = zlib.decompress(zlibdata)
decoded  = cbor2.loads(cbordata)

# print
pprint.pprint(cbor2.loads(decoded.value[2]))
