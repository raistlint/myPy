'''
Created on Apr 30, 2015

@author: rgao

this function use to dump hex data to binary file
which can use in openssl calculation.
'''

import string
import struct

"""
split hex sting to list, byte by byte
"""
def cut(data):
    size = len(data);
    print "size = ", size;
    r = [];
    for i in range(0, size, 2):
        r.append(data[i:i+2])
    return r;

if __name__ == '__main__':
    data = "0EE5C897B6EA0151"
    fp = open("binFile", 'wb')
    map(lambda x: fp.write(struct.pack('B', string.atoi(x, 16))), cut(data))
    fp.close()