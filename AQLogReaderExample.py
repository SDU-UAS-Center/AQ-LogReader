#!/usr/bin/python
# /****************************************************************************
# AQLogReader
# Copyright (c) 2016-2017, Henrik Egemose Schmidt <hes1990@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the copyright holder nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL HENRIK EGEMOSE SCHMIDT BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# ****************************************************************************/
"""
This file is a example of the use for the AutoQuad log file Reader class

Revision:
2017-04-04 Henrik: Test example of the AQLogReader class
"""
# import the class
from AQLogReader import aqLogReader
# Use if export to csv
# import csv

# initilaze the class
aqLC = aqLogReader()

# Select the LOG file. Change the filename to a given LOG file.
aqLC.setLogFile("001-AQL.LOG")

# this command can be used to initilaze the class and load the LOG file.
# aqL = aqLogReader("002-AQL.LOG")

# Use to cahnge to frameRate (number of datapunkts per secund) default is 5.
aqLC.dataFrameRate = 1  # in Hz GPS data is 5 Hz

# Use to change which cahnnels to read from the LOG file.
# default channels is ["GPS_LAT", "GPS_LON", "GPS_HEIGHT"]
aqLC.setChannels(["GPS_LON", "GPS_LAT"])

# Prints a list of all the channels a given LOG file has.
aqLC.printChannelNames()

# Prints the current settings: Which LOG FIle is loaded, what frameRate is
# used and which channels are set to be exported to the data.
aqLC.printCurrentSettings()

# Prints a list of all commands and a short description of what they do.
aqLC.help()

# Gets the data from the LOG file using the current settings.
logData = aqLC.getData()

# Use this if the data is to be exported to csv.
# with open("test.csv", "wb") as f:
#     writer = csv.writer(f)
#     writer.writerows(logData)
