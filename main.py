import os


rootdir = "data"

# read and extract data
for subdir, dirs, files in os.walk("\titanic"):
    print(files)