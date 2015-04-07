#CSVEmailVerifier

* First parameter [mandatory]: the path of the csv file (csv separator column separator as ,)
* Second parameter [mandatory]: the number of the column
* Third parameter: export in two different csv file the output [true|false (default)]
* Forth parameter: jump first line [true|false (default)]

Example: 

```
./csvemailverifier.py ./test.csv 2 true true
```

Output:
```
CSVEmailVerifier 1.0 by Mte90 for Codeat - https://github.com/CodeAtCode
Evaluating in progress
 Email 1 mte90net@gmail.com exist!
 Email 2 fakeuser@domain.tld not exist!
Check in the same path of the input file for the correct.test.csv and wrong.test.csv output file
Processed 2 email in 1 seconds
```

##Requirements

```
pip install python-emailahoy 
```

#SplitCSV

* First parameter [mandatory]: the file
* Second parameter [mandatory]: the lines number

```
splitcsv.py ./test.csv 100
```

Generate the file with pattern [filename]-[number].csv