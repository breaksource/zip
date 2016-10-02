import os
import sys
import util

def collect(node): 
    list = []
    path = os.path.expanduser(node)
    for(dirname,subdir,subfile) in os.walk(path):
        files = []
        for filename in subfile:
            files.append(os.path.join(dirname,filename))
            
        for file in files:
            if file[-4:]=='.jar':
                for x in util.paserOneJar(file):
                    (i,j,name,bas) = x;
                    if bas.find('$') != -1:
                        continue
                    else:
                        list.append(x)
            if file[-6:]== '.class':
                list.append(util.paserOneClassFile(file))
    return list

def printme(list):
    one = '*'
    space = ' '
    for i in range(1,63):
        one = one + '*'
        space = space + ' '
    line = '|' + one + '|'
    text = '|' + space[1:23] + 'class name' + space[1:23] + '|' + 'version' + ' |'
    print line
    print text
    print line
    count = 1
    map = {}
    for (i,j,name,abs) in list:
        var = util.classversion[i]
        if not map.has_key(var):
            map[var] = 1
        else :
            map[var] = map[var] + 1
        print ("|%-7d|%-42s    |%-8s|"%(count,name,util.classversion[i]))
        count = count + 1
    print line
    
    statis = '|' + 'version' + '|' + space[1:27] + 'sum' + space[1:27] +'|'
    print statis
    print line
    keys = sorted(map.keys())
    for key in keys:
        print "|%-6s | %-52s  |" % (key,map[key])
    print line
    
def main(argv):
    currentPath = os.getcwd() + os.sep
    if len(argv)==1:
        printme(collect(currentPath))
    else :
        list = []
        for arg in argv:
            if arg[-4:]=='.jar':
                list.extend(util.paserOneJar(currentPath + arg))
            if arg[-6:]=='.class':
                list.append(util.paserOneClassFile(currentPath + arg))
        printme(list)

if __name__ == '__main__':
    main(sys.argv)