#!/usr/bin/env python3
'''
Two ways of completing Task A
    [1] Zone out and repeat a process of filling a template, researching missing details, and mocking up a test
        - Doing this, I forgot to check if any were IMU-connected
    [2] Attempt a parser factory that applies a generic template, to edit later
        - I had a draft of this on a cloned repository I forgot to save somewhere
        - This is the 2nd attempt at doing this. That draft was buggy anyway.
    
    Yes I did [1] already, but [2] would be good to have on standby.
'''
import csv
from io import StringIO

sensor_table:str = "data-capture/on-car/readers/parsers/Sensor_Status_Tracker.csv"
parser_draft:str = "data-capture/on-car/readers/parsers/parser_product.py"
parser_template:str = """
def parse_{snakecasedSensorName}(data:bytes) -> float:
    '''
    {sensorPlainName} Parser (for {sensorAbbrev})
    Expects _ bytes. Returns {sensorDescription}.
    [source recommended]

    Verify against ECU datasheet
    '''
    raw = data[0]
    conversion = lambda x: x  # Conversion formula recommended
    standard = conversion(raw)
    return standard
"""
tester_template:str = """
def test_{snakecasedSensorName}():
    testBytes = bytes([14, 28])
    result = {sensorParser}(testBytes)
    print(f"{sensorPlainName}:", result)
    assert result == 14, "Expected 14, got " + result
"""

def access_sensor_table(filepath:str, linesIgnored:int=0) -> csv.DictReader:
    """
    Safe Handling of CSV copy of Sensor_Status_Tracker
    Expects:
        filepath - Readable, CSV-formatted sensor table
        linesIgnored - How many CSV lines before fields
    Returns: 
        CSV entry list containing just the headers and sensor rows
    """
    try:
        with open(filepath, 'r') as obj:
            lines = obj.readlines()
    except FileNotFoundError:
        print("parser_factory could not find file {sensor_table}. Try redefining global variable.")
    except Exception as e:
        print("parser_factory encountered error:", e)
    else:
        trimmedCSV = ''.join(lines[linesIgnored:])
        reader = csv.DictReader(StringIO(trimmedCSV))
        return reader

def filter_connected_sensors(reader:csv.DictReader) -> list[dict[str, str]]:
    """
    Outputs sensor dictionary list to match template f-strings
    Expects:
        reader: DictReader object from access_sensor_table()
    Returns:
        Dictionary of CSV entries where connection cells state 'Yes' or 'Partial'
    """
    filteredReader = []
    for entry in reader:
        connectStatus = set((entry["Present on Car"], entry["Connected to IMU"]))
        if connectStatus.issubset({"Yes", "Partial"}):
            filteredReader.append(entry)
    from time import sleep as ts
    for entry in filteredReader:
        print(entry)
        ts(0.1)
    return filteredReader

def madlib_parser_functions(reader:list[dict[str, str]]) -> set[tuple[str]]:
    #  To be used in an iterative process of filling in the blanks of the template f-strings
    #  Once filled, the 'madlibbed parser' is treated as code to be written
    pass
def dump_functional_code():
    #  From a File Handling perspective, appending functional code without organization is nice and easy
    #  This is the super-awesome function that sees a parser_product Python file get coded automatically
    pass
def classify_parsers():
    #  From a further development perspective, appending functional code without organization sucks
    #  This is the super-awesome function that formats a parser_product Python file into a parser_module
    #  that was coded automatically (notice that was done for method [1] of completing Task A)
    pass

if __name__ == "__main__":
    sensors = access_sensor_table(sensor_table, linesIgnored=6)
    viable = filter_connected_sensors(sensors)
    #func_code = madlib_parser_functions(viable)
    #dump_functional_code(func_code)  # type signature tba
    #classify_parsers()  # probably just a generator, I find it satisfying this way
