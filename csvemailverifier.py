#!/usr/bin/python
#CSVEmailVerifier by Mte90
# First parameter [mandatory]: the path of the csv file (csv separator column separator as ,)
# Second parameter [mandatory]: the number of the column
# Third parameter: export in two different csv file the output [true|false (default)]
# Forth parameter: jump first line [true|false (default)]
import sys, os.path, csv, time
from emailahoy import verify_email_address

start_time = time.time()
if len(sys.argv) < 3:
    print("Missing some parameters!")
    sys.exit()

print("CSVEmailVerifier 1.0 by Mte90 for Codeat - https://github.com/CodeAtCode")
#Check file exist
if os.path.isfile(sys.argv[1]):
    with open(sys.argv[1], 'rb') as csvfile:
        print("Evaluating in progress")
        #Prepare the output files
        if len(sys.argv) >= 4:
            if bool(sys.argv[3]):
                correctfile = open(os.path.dirname(sys.argv[1]) + '/correct.' + os.path.basename(sys.argv[1]), "wb")
                correctobject = csv.writer(correctfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                wrongfile = open(os.path.dirname(sys.argv[1]) + '/wrong.' + os.path.basename(sys.argv[1]), "wb")
                wrongobject = csv.writer(wrongfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        #Read the input file
        emailchecking = csv.reader(csvfile, delimiter=',', quotechar='|')
        i = 0
        if len(sys.argv) >= 5:
            if bool(sys.argv[4]):
                i = 1
        for row in emailchecking:
            #Jump the first line that contain the title of the column
            if i != 0:
                actual = row[int(sys.argv[2])]
                if(actual != '') :
                    if verify_email_address(actual.strip()):
                        print(" Email " + str(i-1) + " " + actual + " exist!")
                        #Save the output
                        if len(sys.argv) >= 4:
                            if bool(sys.argv[3]):
                                correctobject.writerow(row)
                    else:
                        print(" Email " + str(i-1) + " " + actual + " not exist!")
                        #Save the output
                        if len(sys.argv) >= 4:
                            if bool(sys.argv[3]):
                                wrongobject.writerow(row)
            else:
                #Inject the first line the output files
                if len(sys.argv) >= 4:
                    if bool(sys.argv[3]):
                        wrongobject.writerow(row)
                        correctobject.writerow(row)
            i += 1
        #Close the output files
        if len(sys.argv) >= 4:
            if bool(sys.argv[3]):
                correctfile.close()
                wrongfile.close()
                print("Check in the same path of the input file for the correct." + os.path.basename(sys.argv[1]) + " and wrong." + os.path.basename(sys.argv[1]) + " output file")
        #File elaboration finished
        calculate = int(time.time() - start_time)
        if calculate == 0:
            calculate = 1
        print("Processed " + str(i - 1) + " email in " + str(calculate) + " seconds" )
else:
    print("The file" + sys.argv[1] + " not exist")
    sys.exit()