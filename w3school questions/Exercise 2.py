# Write a Python program to get the Python version you are using ?
# A string containing the version number of the Python interpreter plus additional information on  the
# build number and compiler used. This string is displayed when the interactive interpreter is started.

import sys

print("python version :- ",sys.version)
# print(sys.version)
print("Version info :- ",sys.version_info)
# print(sys.version_info)

import platform
print(platform.python_version()) # 3.10.5
print(platform.python_version_tuple()) # ('3' , '10' , '5')
print(type(platform.python_version_tuple())) # <class 'tuple'>