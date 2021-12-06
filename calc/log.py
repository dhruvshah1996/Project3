import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
format = logging.Formatter('%(levelname)s %(asctime)s - %(message)s')
fileHandler = logging.FileHandler('testlog.log')
fileHandler.setFormatter(format)
logger.addHandler(fileHandler)
logging.info("Process Started")
#pylint: disable=logging-fstring-interpolation
#pylint: disable=unspecified-encoding
#pylint: disable=f-string-without-interpolation

def logging_data(filename, operation, counter):
    counter = counter+1
    with open('testlog.log','a') as appendFile:
        appendFile.write(f'Filename: {filename} -Record Number: {counter} -TestRan: {operation}\n ')

    return appendFile
logger.info(f"Test Saved successfully")