from ftplib import FTP
import os, sys, os.path

def handleDownload(block):
    file.write(block)
    print ".",

ddir='/Users' # set to local path where you want files downloaded to
os.chdir(ddir)
ftp = FTP('avng.jpl.nasa.gov')

print 'Logging in.'
ftp.login()
directory = '/AVNG_2015_data_distribution/L2/'
print 'Changing to ' + directory
ftp.cwd(directory)

dirnames = ftp.nlst() # get list of directories
print dirnames

#for each directory, download the directory and its contents to local computer
for dirname in dirnames:
    print 'Changing to ' + dirname
    ftp.cwd(dirname)
    filenames = ftp.nlst() # get list of filenames in directory
    print filenames
    count = 0
    localpath = ddir + '/' + dirname
    os.mkdir(localpath) # create this directory locally
    #download each file to the newly created local directory
    for filename in filenames:
        local_filename = os.path.join(localpath, filename)
        file = open(local_filename, 'wb')
        ftp.retrbinary('RETR '+ filename, file.write)
        file.close()

    ftp.cwd('..')

ftp.quit()

