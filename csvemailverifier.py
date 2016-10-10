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

from email_validator import validate_email

start_time = time.time()
if len(sys.argv) < 3:
    print("CSVEmailVerifier by Mte90")
    print("First parameter [mandatory]: the path of the csv file (csv separator column separator as ,)")
    print("Second parameter [mandatory]: the number of the email column")
    print("Third parameter: export in two different csv file the output [true|false (default)]")
    print("Forth parameter: jump first line [true|false (default)]")
    sys.exit()

print("CSVEmailVerifier 1.0 by Mte90 for Codeat - https://github.com/CodeAtCode")


def validate(email):
    try:
        validate_email(email)
    except:
        return False
    return True


# Check if file exists
if os.path.isfile(sys.argv[1]):
    file = sys.argv[1]
    position = int(sys.argv[2])      # Column no. for the email
    to_jump = False
    to_write = False
    if len(sys.argv) >= 4 and sys.argv[3].lower() == 'true':
        to_write = True
    if len(sys.argv) == 5 and sys.argv[4].lower() == 'true':
        to_jump = True

    with open(file, 'rb') as csv_file:
        print("Evaluating in progress...")
        # Prepare the output files
        if to_write:
            dirname = os.path.dirname(file)
            if(dirname == '.'):
                dirname = ''
            correct_file = open(dirname + './correct.' + os.path.basename(file), "wb")
            correct_object = csv.writer(correct_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            wrong_file = open(dirname + './wrong.' + os.path.basename(file), "wb")
            wrong_object = csv.writer(wrong_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        # Read the input file
        email_checking = csv.reader(csv_file, delimiter=',', quotechar='|')
        line_no = 0
        for row in email_checking:
            line_no += 1
            # Reading the first line that contain the title of the column
            if line_no == 1:
                if not(to_jump) and to_write:
                    wrong_object.writerow(row)
                    correct_object.writerow(row)
            else:
                email = row[position]
                if email != '':
                    if validate(email.strip()):
                        print(" Email " + str(line_no - 1) + " " + email + " exists!")
                        # Save the output
                        if to_write:
                            correct_object.writerow(row)
                            correct_file.flush()
                    else:
                        print(" Email " + str(line_no - 1) + " " + email + " not exists!")
                        # Save the output
                        if to_write:
                            wrong_object.writerow(row)
                            wrong_file.flush()

        if to_write:
            correct_file.close()
            wrong_file.close()
            print("Check in the same path of the input file for the correct." + os.path.basename(
                file) + " and wrong." + os.path.basename(file) + " output file")
        # File elaboration finished
        calculate = int(time.time() - start_time)
        if calculate == 0:
            calculate = 1
        print("Processed " + str(line_no - 1) + " emails in " + str(calculate) + " seconds")

else:
    print("The file" + sys.argv[1] + " does not exist")
    sys.exit()
