#!/usr/bin/python
# First parameter: the pattern for the files in ""
# Second parameter: output file
import glob
import sys

read_files = sorted(glob.glob(sys.argv[1]))

with open(sys.argv[2], "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

print("File generated")
