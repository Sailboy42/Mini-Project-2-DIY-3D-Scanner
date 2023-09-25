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
    lineOfData = serialPort.readline().decode()

    #
    # check if data was received
    #
    if len(lineOfData) > 0:
        #
        # data was received, convert it into 4 integers
        #
        a, b, c, d = (int(x) for x in lineOfData.split(","))

        # list of name, degree, score
        nme = ["aparna", "pankaj", "sudhir", "Geeku"]
        deg = ["MBA", "BCA", "M.Tech", "MBA"]
        scr = [90, 40, 80, 98]

        # dictionary of lists
        dict = {"name": nme, "degree": deg, "score": scr}

        df = pd.DataFrame(dict)

        print(df)

        df.to_csv("file1.csv")
