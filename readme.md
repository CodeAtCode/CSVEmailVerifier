#CSVEmailVerifier by Mte90

* First parameter [mandatory]: the path of the csv file (csv separator column separator as ,)
* Second parameter [mandatory]: the number of the column
* Third parameter: export in two different csv file the output [true|false (default)]

Example: 

```
./csvemailverifier.py ./test.csv 2 true
```

Output:
```
CSVEmailVerifier 1.0 by Mte90 for Codeat - https://github.com/CodeAtCode
Evaluating in progress
 Email mte90net@gmail.com exist!
 Email fakeuser@domain.tld not exist!
Check in the same path of the input file for the correct.test.csv and wrong.test.csv output file
Processed 2 email in 1 seconds
```

##Requirements

```
pip install python-emailahoy 
```
