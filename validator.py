# A simple 10 digit telephone number validator
# Fred T. Dunaway
# Dec 23, 2021
# Regular expression taken from:  https://stackoverflow.com/questions/16699007/regular-expression-to-match-standard-10-digit-phone-number/16702965

import argparse
import logging
import logging.handlers
import re

parser = argparse.ArgumentParser()
parser.add_argument("--log_level", 
                    help="The level of log messages to log", 
                    default="INFO", 
                    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'])
parser.add_argument("--inputFile",
                    help="The file containing a list of telephone numbers, one line per number", 
                    default="phoneNumbers.txt" )

args = parser.parse_args()
LOG_FILENAME = 'phoneValidator.log'
ml = logging.getLogger('Logger')
ml.setLevel(level = args.log_level)
logFormatter = logging.Formatter('%(levelname)s\t%(asctime)s\t%(message)s')
logHandler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=20000000, backupCount=2 )
logHandler.setFormatter(logFormatter)
ml.addHandler(logHandler)

p = re.compile('^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$' )
try: 
    file1 = open(args.inputFile, 'r')
    count = 0
    for line in file1:
        count += 1
        phoneNum = line.strip()
        m = p.match(phoneNum)
        if m:
            ml.debug('Telephone number {} is valid.'.format(phoneNum))
        else:
            ml.info('Telephone number "{}" failed validation'.format(phoneNum))
            print('Telephone number "{}" failed validation'.format(phoneNum))
    
    file1.close()

except Exception as e: 
    print('Error: {}'.format(e))
    ml.error('Error of {}'.format(e))
