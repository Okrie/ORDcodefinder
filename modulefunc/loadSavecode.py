import os, sys, time

from modulefunc.printResult import printresult
from . import printResult

def loadFile():
    try:
        path_dir = os.path.expanduser('~\Documents\Warcraft III\CustomMapData\ORD11')

        # Get list of all files only in the given directory
        list_of_files = filter( lambda x: os.path.isfile(os.path.join(path_dir, x)),
                            os.listdir(path_dir) )

        # Sort list of files based on last modification time in ascending order
        list_of_files = sorted( list_of_files, key = lambda x: os.path.getmtime(os.path.join(path_dir, x)))
        
        for file_name in list_of_files:
            file_path = os.path.join(path_dir, file_name)
            timestamp_str = time.strftime(  '%m/%d/%Y :: %H:%M:%S', time.gmtime(os.path.getmtime(file_path))) 
            
        print(timestamp_str, ' --> ', file_name)
        saveCodeFile = file_name
        print(saveCodeFile)
        
        f = open(path_dir + '\\' + saveCodeFile, 'r', encoding='utf8')
        codeline = f.readlines()[6]
        saveCodeStr = codeline[16:-4]
        f.close()

        printResult.printresult(saveCodeStr)
    except Exception as e:
        print(e)