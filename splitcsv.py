#!/usr/bin/python
# Based on http://stackoverflow.com/a/20034173/1902215
# First parameter: the file
# Second parameter: the lines number
import csv
import os
import sys

divisor = int(sys.argv[2])

outfile_no = 1
outfile = None

if os.path.isfile(sys.argv[1]):
    with open(sys.argv[1], 'r') as infile:
        for index, row in enumerate(csv.reader(infile)):
            if index % divisor == 0:
                if outfile is not None:
                    outfile.close()
                outfile_name = os.path.splitext(sys.argv[1])[0] + '-{}.csv'.format(outfile_no)
                outfile = open(outfile_name, 'w')
                outfile_no += 1
                writer = csv.writer(outfile)
            writer.writerow(row)

    print('Done')
else:
    print("The file" + sys.argv[1] + " not exist")
    sys.exit()
