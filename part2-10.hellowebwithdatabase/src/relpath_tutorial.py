import os
import sys

#source: https://www.delftstack.com/howto/python/relative-path-in-python/
#documentation: https://docs.python.org/3/library/os.path.html

absolutepath = os.path.abspath(__file__)
print("\n absolutepath: ", absolutepath) # prints current path incl. filename


print("\n\n dirname raw:", os.path.dirname(os.path.dirname(__file__)))

fileDirectory = os.path.dirname(absolutepath)
print("\n\n fileDirectory:", fileDirectory)

parentDirectory = os.path.dirname(fileDirectory)
print("\n\n parentDirectory:", parentDirectory)

newPath = os.path.join(parentDirectory, 'Strings')   
print("\n\n newPath:", newPath)
