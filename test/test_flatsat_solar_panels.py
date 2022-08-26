'''
 * Copyright (C) 2021  University of Alberta
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
'''
'''
 * @file test_flatsat_solar_panels.py
 * @author Daniel Sacro
 * @date 2022-03-14
'''
from groundstation_tester import Tester
from test_full_hk import testSystemWideHK

tester = Tester() #call to initialize local test class

def testAllCommandsToOBC():
    print("\n---------- OBC SYSTEM-WIDE HOUSEKEEPING TEST ----------\n")
    testSystemWideHK(1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0)

    tester.summary() #call when done to print summary of tests

if __name__ == '__main__':
    testAllCommandsToOBC()
