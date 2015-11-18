#!/usr/bin/python/2.7
import time
import sys
import os
import os.path
import re

# start of training utt in seconds (HATS track): 6, 19, 32, 45
# when to poke record button in seconds: 4, 17, 30, 43

B = time.asctime()
print "Training started at %s" % B
def main():
    start = int(time.time()) 
    while True:
        delta_t = int(time.time()) - start
        if delta_t == 4:
            print "Record 1"
            os.system('parallel ./train ::: 03157df383d8893b 03157df3c1565c04 03157df3c0c51131 ::: 640 ::: 430')
	elif delta_t == 17:
	    print "Record 2"
	    os.system('parallel ./train ::: 03157df383d8893b 03157df3c1565c04 03157df3c0c51131 ::: 1050 ::: 430')
        elif delta_t == 30: 
	    print "Record 3"
	    os.system('parallel ./train ::: 03157df383d8893b 03157df3c1565c04 03157df3c0c51131 ::: 230 ::: 660')
        elif delta_t == 43:
	    print "Record 4"
	    os.system('parallel ./train ::: 03157df383d8893b 03157df3c1565c04 03157df3c0c51131 ::: 640 ::: 660')
        elif delta_t == 55:
            print "Training"
	    os.system('parallel ./train ::: 03157df383d8893b 03157df3c1565c04 03157df3c0c51131 ::: 1110 ::: 660')              
        else:
            time.sleep(1)
            if delta_t >= 60:
                break
    print "Training completed"

if __name__ == '__main__':
    main()
