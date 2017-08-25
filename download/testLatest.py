#!/usr/bin/env python

import os, errno
import urllib2
import urlparse, urllib
import hashlib
import sys
import argparse
import urllib, json
from distutils.version import StrictVersion
from subprocess import call

parser = argparse.ArgumentParser(description='USB Stick Download site creator test.')
parser.add_argument('--path', help='Specify URL of the versions.json file', required=True)

args = parser.parse_args()


with open(args.path) as jdata:
	data = json.load(jdata)
	keys =  data.keys()
	keys.sort(key=StrictVersion)
	print keys
        returnCode = call(["python", "create-usb.py","--url","file:"+data[keys[-1]]])
        sys.exit(returnCode)
        
