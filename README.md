# autopyc v1.0.0
This is a small script to automatically compile your Python code using py_compile, useful to deploy compiled code without sharing the sources.

It is useful for big projects, with a lot of .py files, in fact running "python -m compileall" would compile the sources, but storing the .pyc in __pycache__ folders and subfolders.

This script instead will prepare the output folder by creating a new project folder with just the compiled files in place of the sources.

--+ProjectFolder
  |
  +--main.py
  |
  +--Folder1
  |  |
  |  +--sub1.py
  |  +--sub2.py
  |   
  +--Folder2
     |
     +--sub3.py
     +--sub4.py
     
     
     
python autopyc.py -d ProjectFolder

--+ProjectFolder_autopyc
  |
  +--main.pyc
  |
  +--Folder1
  |  |
  |  +--sub1.pyc
  |  +--sub2.pyc
  |   
  +--Folder2
     |
     +--sub3.pyc
     +--sub4.pyc

using the option "-i" compiling can be done in-place without creating a new folder (warning, using this option all .py files will be deleted and replaced by .pyc files)
