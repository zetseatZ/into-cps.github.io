#!/usr/bin/env python
#
# Download script to generate a USB version of the complete download version
#
#
import os, errno
import urllib2
import urlparse, urllib
import hashlib
import sys
import argparse
import urllib, json
import socket

parser = argparse.ArgumentParser(description='USB Stick Download site creator.')
parser.add_argument('--url', help='Specify URL of the download file', required=True)
parser.add_argument('--skip', help='Skip download of the tool bundles', action='store_true')


def path2url(path):
    return urlparse.urljoin(
        'file:', urllib.pathname2url(path))

def human_size(bytes, units=[' bytes','KB','MB','GB','TB', 'PB', 'EB']):
    """ Returns a human readable string reprentation of bytes"""
    return str(bytes)+units.pop(0) if bytes < 1024 else human_size(bytes>>10, units[1:])

def downloadFile(url,outputPath,indent):
    try:
        u = urllib2.urlopen(url)
        meta = u.info()
        file_size = int(meta.getheaders('Content-Length')[0])

        # save downloaded file to TEMP directory
        f = open(outputPath, 'wb')
    
        downloaded_bytes = 0
        block_size = 1024*8
        downloaded_bytes2=0
        step = file_size /25
        while True:
            buffer = u.read(block_size)
            if not buffer:
                break
        
            f.write(buffer)
            downloaded_bytes += block_size

            if downloaded_bytes2+step < downloaded_bytes: 
                print "%sDownloaded %s of %s" %(("\t" * indent),human_size(downloaded_bytes),human_size(file_size))
                downloaded_bytes2 = downloaded_bytes
        f.close()
        return True
    except urllib2.HTTPError, err:
        print "%sHTTP Error code: %d" % (("\t" * indent),err.code)
    except urllib2.URLError, err:
        print "%sDownload Error reason: %s" % (("\t" * indent),err.reason)
    except socket.error, e:
        print "%sDownload Error: %r" % (("\t" * indent),e)
    return False

args = parser.parse_args()


url = args.url

downloadFailures=False

response = urllib.urlopen(url)
data = json.loads(response.read())
#print data

version = data["version"];
print "Processing version: %s" % version

for tool in data["tools"]:
    print "\tProcessing tool %s" % tool
    for p in data["tools"][tool]["platforms"]:
        url = data["tools"][tool]["platforms"][p]["url"]
        name = data["tools"][tool]["platforms"][p]["filename"]
        md5sum = data["tools"][tool]["platforms"][p]["md5sum"]
        print "\t\tPlatform: %s" % p
        directory = os.path.join("usb",version,tool,p)
        if not os.path.exists(directory):
            os.makedirs(directory)
        #urlShort = ('..'+url[75:] ) if len(url) > 75 else url
        urlShort = url[:75] + bool(url[75:]) * '..'
        print "\t\t\tDownloading %s from %s" %(name,urlShort)
        outFile = os.path.join(directory,name)
        print "\t\t\t\tOutput path: %s" % outFile
        md5 = hashlib.md5(open(outFile).read()).hexdigest() if os.path.exists(outFile) else ""
        #print md5
        if md5 != md5sum:
            if os.path.exists(outFile):
                print "%sError CRC mismatch expected: %s got %s" % (("\t" * 4),md5sum,md5)
            if not args.skip:
                if not downloadFile(url,outFile,4):
                    downloadFailures = True
        else:
            print "%sCRC OK" % ("\t" * 4)
        data["tools"][tool]["platforms"][p]["url"] = path2url(outFile).replace("file:///usb/","file:")
        md5 = hashlib.md5(open(outFile).read()).hexdigest() if os.path.exists(outFile) else ""
        if md5 != md5sum:
            print "%sCRC Error %s" % (("\t" * 4),outFile)
            downloadFailures = True

print "Writing modified version info for %s" %version
with open(os.path.join("usb",version+".json"), 'w') as outfile:
    json.dump(data, outfile)

print "Writing top versions.json file"

ov = {}
ov[version]=version+".json"
with open(os.path.join("usb","versions.json"), 'w') as outfile:
    json.dump(ov, outfile)

if downloadFailures:
    sys.exit(1)
