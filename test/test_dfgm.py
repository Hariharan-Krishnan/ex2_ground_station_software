'''  to run > yarn run:test_dfgm -I uart -d /dev/ttyUSB0 '''

import numpy as np

import sys
from os import path
sys.path.append("./test")

from testLib import testLib as test

import time

test = test() #call to initialize local test class

def testAllCommandsToOBC():
    # Basic functionality tests
    test.send('obc.dfgm.dfgm_get_hk') # Update empty HK buffer by turning on DFGM for 1 sec
    time.sleep(2)

    test.send('obc.dfgm.dfgm_get_hk') # Should instantly get updated data from the HK buffer

    test.sendAndExpect('obc.dfgm.dfgm_run(1)', {'err': 0})
    time.sleep(2)

    test.sendAndExpect('obc.dfgm.dfgm_run(10)', {'err': 0})
    time.sleep(11) 

    test.sendAndExpect('obc.dfgm.dfgm_run(2147483647)', {'err': 0}) # INT_MAX
    time.sleep(1)
    test.sendAndExpect('obc.dfgm.dfgm_stop', {'err': 0}) # Check if DFGM actually stops dfgm_run

    test.sendAndExpect('obc.dfgm.dfgm_start', {'err': 0})
    time.sleep(5) # Let DFGM run for a bit

    test.sendAndExpect('obc.dfgm.dfgm_stop', {'err': 0}) # Check if DFGM actually stops dfgm_start

    test.send('obc.dfgm.dfgm_get_hk') # Check if data gets corrupt somehow (temp. should be ~20, not ~65000)


    # Error checking tests
    test.sendAndExpect('obc.dfgm.dfgm_run(2147483648)', {'err': 1}) # Bad param. - Overflow for 32-bit int
    test.sendAndExpect('obc.dfgm.dfgm_run(0)', {'err': 1}) # Bad param. - Less than minRuntime

    test.sendAndExpect('obc.dfgm.dfgm_run(100)', {'err': 0})
    test.sendAndExpect('obc.dfgm.dfgm_start', {'err': 2}) # Busy - DFGM already running
    test.sendAndExpect('obc.dfgm.dfgm_run(1000)', {'err': 2}) # Busy

    test.send('obc.dfgm.dfgm_get_hk') # See if any of the values get updated from other packets
    test.sendAndExpect('obc.dfgm.dfgm_stop', {'err': 0}) 

    test.sendAndExpect('obc.dfgm.dfgm_stop', {'err': 0}) # Should not fail if nothing is running


    test.summary() #call when done to print summary of tests


if __name__ == '__main__':
    testAllCommandsToOBC()
