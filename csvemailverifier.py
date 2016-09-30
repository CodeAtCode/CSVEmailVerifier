#!/usr/bin/python
# CSVEmailVerifier by Mte90
# First parameter [mandatory]: the path of the csv file (csv separator column separator as ,)
# Second parameter [mandatory]: the number of the email column
# Third parameter: export in two different csv file the output [true|false (default)]
# Forth parameter: jump first line [true|false (default)]
import csv
import os.path
import sys
import time

from emailahoy import verify_email_address

start_time = time.time()
if len(sys.argv) < 3:
    print("CSVEmailVerifier by Mte90")
    print("First parameter [mandatory]: the path of the csv file (csv separator column separator as ,)")
    print("Second parameter [mandatory]: the number of the email column")
    print("Third parameter: export in two different csv file the output [true|false (default)]")
    print("Forth parameter: jump first line [true|false (default)]")
    sys.exit()

print("CSVEmailVerifier 1.0 by Mte90 for Codeat - https://github.com/CodeAtCode")
# Check file exist
if os.path.isfile(sys.argv[1]):
    with open(sys.argv[1], 'rb') as csv_file:
        print("Evaluating in progress")
        # Prepare the output files
        if len(sys.argv) >= 4:
            if bool(sys.argv[3]):
                correct_file = open(os.path.dirname(sys.argv[1]) + './correct.' + os.path.basename(sys.argv[1]), "wb")
                correct_object = csv.writer(correct_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                wrong_file = open(os.path.dirname(sys.argv[1]) + './wrong.' + os.path.basename(sys.argv[1]), "wb")
                wrong_object = csv.writer(wrong_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        # Read the input file
        email_checking = csv.reader(csv_file, delimiter=',', quotechar='|')
        i = 0
        if len(sys.argv) >= 5:
            if bool(sys.argv[4]):
                i = 1
        for row in email_checking:
            # Jump the first line that contain the title of the column
            if i == 1:
                pass
            elif i != 0:
                actual = row[int(sys.argv[2])]
                if actual != '':
                    if verify_email_address(actual.strip()):
                        print(" Email " + str(i - 1) + " " + actual + " exist!")
                        # Save the output
                        if len(sys.argv) >= 4:
                            if bool(sys.argv[3]):
                                correct_object.writerow(row)
                                correct_file.flush()
                    else:
                        print(" Email " + str(i - 1) + " " + actual + " not exist!")
                        # Save the output
                        if len(sys.argv) >= 4:
                            if bool(sys.argv[3]):
                                wrong_object.writerow(row)
                                wrong_file.flush()
            else:
                # Inject the first line the output files
                if len(sys.argv) >= 4:
                    if bool(sys.argv[3]):
                        wrong_object.writerow(row)
                        correct_object.writerow(row)
            i += 1
        # Close the output files
        if len(sys.argv) >= 4:
            if bool(sys.argv[3]):
                correct_file.close()
                wrong_file.close()
                print("Check in the same path of the input file for the correct." + os.path.basename(
                    sys.argv[1]) + " and wrong." + os.path.basename(sys.argv[1]) + " output file")
        # File elaboration finished
        calculate = int(time.time() - start_time)
        if calculate == 0:
            calculate = 1
        print("Processed " + str(i - 1) + " email in " + str(calculate) + " seconds")
else:
    print("The file" + sys.argv[1] + " not exist")
    sys.exit()
