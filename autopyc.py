import py_compile
import shutil
import sys, os
import argparse
from fnmatch import fnmatch

print("Autopyc v1.0.0 - Python Compiler automator")

parse = argparse.ArgumentParser()
parse.add_argument("-i",help="compile in-place",action="store_true")
parse.add_argument("-d",help="folder to be compiled",required=True)
args = parse.parse_args()
if(args.i):
    destpath = args.d
else:
    if args.d.endswith('/'):
        destpath = args.d[:-1] + "_autopyc"
    else:
        destpath = args.d + "_autopyc"
    try:
        shutil.copytree(args.d,destpath)
    except:
        print("Can't create compiled folder")

pattern = "*.py"
compiled_files = 0

for path, subdirs, files in os.walk(destpath):
    for name in files:
        if fnmatch(name, pattern):
            filename = os.path.join(path, name)
            print('compiling ' + filename)
            py_compile.compile(filename,cfile=filename+"c")
            os.remove(filename)
            compiled_files += 1
    for subdir in subdirs:
        if(subdir == '__pycache__'):
            cachepath = os.path.join(path,subdir)
            shutil.rmtree(cachepath)

print("Total compiled files: " + str(compiled_files))

