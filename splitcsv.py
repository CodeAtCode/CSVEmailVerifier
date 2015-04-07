#!/usr/bin/python
#based on http://stackoverflow.com/a/20034173/1902215
#first parameter: the file
#second parameter: the lines
import csv, sys, os

divisor = int(sys.argv[2])

outfileno = 1
outfile = None

if os.path.isfile(sys.argv[1]):
    with open(sys.argv[1], 'r') as infile:
        for index, row in enumerate(csv.reader(infile)):
            if index % divisor == 0:
                if outfile is not None:
                    outfile.close()
                outfilename = os.path.splitext(sys.argv[1])[0] + '-{}.csv'.format(outfileno)
                outfile = open(outfilename, 'w')
                outfileno += 1
                writer = csv.writer(outfile)
            writer.writerow(row)

    print('Done')
else:
    print("The file" + sys.argv[1] + " not exist")
    sys.exit()