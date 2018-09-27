import os

try:
    if not(os.path.isdir("test_directory")):
        os.makedirs(os.path.join("test_directory"))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("failed to create directory!!")
        raise