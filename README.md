# Telephone Number Validator
A simple utility to validate a list of 10 digit phone numbers in a file.  One phone number per line.
The regular expresion was taken from: [stack over flow] (https://stackoverflow.com/questions/16699007/regular-expression-to-match-standard-10-digit-phone-number/16702965)

Fred T. Dunaway
Dec 23, 2021

## Requires
* Python 3.x

## Use
1. Clone this repository.
1. Change directory to wherever the repository was cloned to on your local machine.
1. Create a file containing a list of the telephone numbers to be validated.  The default is 'phoneNumbers.txt'
1. run:  python3 validator.py --inputFile=<file with your phone numbers>
1. Invalid telephone numbers will be printed to stdout

## Arguments
-   -h, --help                               show this help message and exit
-  --log_level {DEBUG,INFO,WARNING,ERROR}    The level of log messages to log
-  --inputFile INPUTFILE                     The file containing a list of telephone numbers, one line per number
