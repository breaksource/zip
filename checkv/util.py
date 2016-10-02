
import binascii
import os
import zipfile


def paserOneJar(filename):
    jar = []
    z = zipfile.ZipFile(filename,'r');
    for name in z.namelist():
        pos = name.rfind('.class')
        if (pos != -1):
            line = z.read(name)
            hex = binascii.hexlify(line)
            jar.append(cutVersionNum(hex) + cutFilename(name))
    return jar
   
def paserOneClassFile(filename):
    file = open(filename)
    try:
        text = file.read()
        hex = binascii.hexlify(text)
        return cutVersionNum(hex) + cutFilename(filename)
    finally:
        file.close()

def cutVersionNum(sequance):
    if sequance.strip() and len(sequance)>16:
        return (sequance[14:16],sequance[12:14])
    else:
        return None

def cutFilename(absoluteFilename):
    if (absoluteFilename.strip()):
        ret = absoluteFilename.replace('/',os.sep)
        absoluteFilename = ret.replace('\\',os.sep)
        pathArray = absoluteFilename.split(os.sep)
        if len(pathArray)>0:
            return (pathArray[len(pathArray)-1],absoluteFilename)
    else:
        return None

#java version 
classversion = {}
classversion['2d'] = '1.1'
classversion['2e'] = '1.2'
classversion['2f'] = '1.3'
classversion['30'] = '1.4'
classversion['31'] = '1.5'
classversion['32'] = '1.6'
classversion['33'] = '1.7'
classversion['34'] = '1.8'
classversion['35'] = '1.9'
classversion['36'] = '2.0'
classversion['37'] = '2.1'
classversion['38'] = '2.2'
classversion['39'] = '2.3'
classversion['40'] = '2.4'
classversion['41'] = '2.5'
classversion['42'] = '2.6'
classversion['43'] = '2.7'
classversion['44'] = '2.8'
classversion['45'] = '2.9'
classversion['46'] = '3.0'
classversion['47'] = '3.1'
classversion['48'] = '3.2'
classversion['49'] = '3.3'
classversion['50'] = '3.4'