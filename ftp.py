# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 08:52:32 2014

@author: Daniel
"""

import os, time, operator, ftplib 


#=====

import sys, os, time, ftplib
import collections
FTPDir= collections.namedtuple("FTPDir", "name size mtime tree")
FTPFile= collections.namedtuple("FTPFile", "name size mtime")

"""class FTPDirectory(object):
    def __init__(self, path='.'):
        self.dirs= []
        self.files= []
        self.path= path

    def getdata(self, ftpobj):
        ftpobj.retrlines('MLSD', self.addline)

    def addline(self, line):
        data, _, name= line.partition('; ')
        fields= data.split(';')
        for field in fields:
            field_name, _, field_value= field.partition('=')
            if field_name == 'type':
                target= self.dirs if field_value == 'dir' else self.files
            elif field_name in ('sizd', 'size'):
                size= int(field_value)
            elif field_name == 'modify':
                mtime= time.mktime(time.strptime(field_value, "%Y%m%d%H%M%S"))
        if target is self.files:
            target.append(FTPFile(name, size, mtime))
        else:
            size= int(field_value)
            target.append(FTPDir(name, size, mtime, self.__class__(os.path.join(self.path, name))))

    def walk(self):
        for ftpfile in self.files:
            yield self.path, ftpfile
        for ftpdir in self.dirs:
            for path, ftpfile in ftpdir.tree.walk():
                yield path, ftpfile

class FTPTree(FTPDirectory):
    def getdata(self, ftpobj):
        super(FTPTree, self).getdata(ftpobj)
        for dirname in self.dirs:
            ftpobj.cwd(dirname.name)
            dirname.tree.getdata(ftpobj)
            ftpobj.cwd('..')"""
            
#=====

dir1="C:\\D1"

user = 'bwb0de'
host = 'localhost'
passw = 'm@r1anell4'

os.chdir(dir1)

try:
    ftp = ftplib.FTP(host)
    aftp = ftplib.FTP
    ftp.login(user, passw)
    print "FTP logado como %s@%s!" % (user, host)
except:
    print "FTP erro na conexão!"



'''def listftpfiles():
    data=[]
    output=[]
    ftp.dir(data.append)
    for line in data:
        timeinfo, filename = line.split(':')[0][-9:]+':'+line.split(':')[1][0:2], line.split(':')[1][3:]
        date_str = ' '.join(line.split()[5:8])
        timetupla = time.strptime(date_str, '%b %d %H:%M') # import time
        output.append((timeinfo, filename, timetupla))
    return output
    
l = listftpfiles()
print l

 #ftp.retrbinary('RETR README', open('README', 'wb').write)'''