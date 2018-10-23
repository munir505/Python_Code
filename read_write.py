#!/bin/python
import os
file_m = open('write_to.txt', 'a')
for x in os.listdir('/proc'):
        if x.isdigit():
                path = "/proc/"+x+"/status"
                #fp = open(path, 'r')
                #print(fp.read())
                with open(path) as fp:
                        line = fp.readline()
                        print("Pid: " +  x)
                        print(line)
                        fp.close()
                        file_m.write("Pid: " +  x + ", ")
                        file_m.write(line)
file_m.close()