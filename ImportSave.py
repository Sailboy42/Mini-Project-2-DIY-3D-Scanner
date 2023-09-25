import serial
import pandas as pd

arduinoComPort = "COM6"
baudRate = 9600
serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)

while True:
    #
    # ask for a line of data from the serial port, the ".decode()" converts the
    # data from an "array of bytes", to a string
    #
    ScanData = serialPort.readline().decode()

    #
    # check if data was received
    #
    if len(ScanData) > 0:
        df = pd.DataFrame(ScanData)  # convert list to dataframe

        """***************************************************************************************
        *    Title: Pandas tocsv Checking for Overwrite Using Mode Paramter
        *    Author: Saturn Cloud
        *    Date: Monday, June 19, 2023
        *    Code version: 1
        *    Availability: https://saturncloud.io/blog/pandas-tocsv-checking-for-overwrite/
        *
        ***************************************************************************************"""
        file_path = "3DScan"

        try:
            df.to_csv(file_path, index=False, mode="x")
            print(f"The file '{file_path}' has been created.")
        except FileExistsError:
            overwrite = input(
                f"The file '{file_path}' already exists. Do you want to overwrite it? (y/n): "
            )
            if overwrite.lower() == "y":
                df.to_csv(file_path, index=False, mode="w")
                print(f"The file '{file_path}' has been overwritten.")
            else:
                print(f"The file '{file_path}' has not been overwritten.")
