#!/usr/bin/python/2.7
import time
import sys
import os
import os.path
import re
import signal

#################################################################################################
total_n = 40.0  # number of KWs per case
total_t = 596  # length  of each case in seconds, 4seconds reserved for app relaunch.

device = ['03157df383d8893b', '03157df3c1565c04', '03157df3c0c51131']
case = ['Clean', 'Car0', 'Babble0', 'Car6', 'Babble6', 'Car12', 'Babble12'] 
#case = ['Babble0'] 

outDir = '/home/shon2/workspace/aVoiceQ' # output directory
FW = 'avoiceq_v2.4'  # test FW
KW = 'U5_K5_E_FT_retrainedKW'  # test KW
dirname = os.path.join(outDir, KW + '_' + FW)
##################################################################################################
print "test directory: %s" % outDir
#os.system('parallel ./shot_restartApp ::: 03157df383d8893b 03157df3c1565c04 #03157df3c0c51131 ::: Init')


def shots(value, start_t):
    print "\nStart shots and relaunch: %s \n" % (time.asctime())
    os.system('mkdir -p shots/' + value)
    os.system('parallel ./shot_restartApp ::: 03157df383d8893b 03157df3c1565c04 03157df3c0c51131 ::: '+ value)
    print "\nEnd shots and relaunch: %s \n" % (time.asctime()) 
    
    #f = open(fname, 'a')
    #f.write("Noise: %s" % value)
    #f.write("\nStart time: %s" % (start_t))
    #f.write("\nEnd time: %s \n" % (time.asctime()))
    #f.write("\n==================================================\n\n")
    #f.close()
    

def KWcount(value):
    start_t = time.asctime()
    start = time.time()
    print "\nNoise: %s \nStart time: %s" % (value, start_t)
    while True:
        delta_t = time.time() - start
        if int(delta_t) >= total_t:
            print "\nEnd time: %s \n" % (time.asctime()) 
            break 
    shots(value, start_t)


def main():     
    for value in case:
        KWcount(value)
    os.system('mv shots ' + dirname)

if __name__ == '__main__':
    main()

