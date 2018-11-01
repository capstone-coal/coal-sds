# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ftplib import FTP
import os, sys, os.path

def handleDownload(block):
    file.write(block)
    print ".",

ddir='/Users/alexahuerta/Documents' # set to local path where you want files downloaded to
os.chdir(ddir)
ftp = FTP('avng.jpl.nasa.gov')

print 'Logging in.'
ftp.login()
directory = '/'

flight_line = raw_input("Enter name of flight line you wish to download: ")
data2014 = '/AVNG_2014_data_distribution/L2/'
data2015 = '/AVNG_2015_data_distribution/L2/'

ftp.cwd(data2015)
dirnames2015 = ftp.nlst()
for dirname in dirnames2015:
    if dirname == flight_line:
        print 'Changing to ' + dirname
        ftp.cwd(dirname)
        filenames = ftp.nlst() # get list of filenames in directory
        print filenames
        localpath = ddir + '/' + dirname
        print localpath
        os.mkdir(localpath) # create this directory locally
        #download each file to the newly created local directory
        for filename in filenames:
            local_filename = os.path.join(localpath, filename)
            file = open(local_filename, 'wb')
            ftp.retrbinary('RETR '+ filename, file.write)
            file.close()
        ftp.cwd('../..')

ftp.cwd(data2014)
dirnames2014 = ftp.nlst()
for dirname in dirnames2014:
    if dirname == flight_line:
        print 'Changing to ' + dirname
        ftp.cwd(dirname)
        filenames = ftp.nlst() # get list of filenames in directory
        print filenames
        localpath = ddir + '/' + dirname
        print localpath
        os.mkdir(localpath) # create this directory locally
        #download each file to the newly created local directory
        for filename in filenames:
            local_filename = os.path.join(localpath, filename)
            file = open(local_filename, 'wb')
            ftp.retrbinary('RETR '+ filename, file.write)
            file.close()
        ftp.cwd('../..')

ftp.quit()
