import csv

with open("gps_source.txt", "r") as inFile:
    csv_reader = csv.reader(inFile, delimiter=":")
    lineNum = 1
    for row in csv_reader:
        row[2] = float(row[2])
        row[2] += 2000
        row[2] = str(row[2])

        row[1] = str("Station " + str(lineNum))
        print(row[1])
        lineNum += 1
        print(row)
        with open("Outfile.txt", "a") as data:
            data.write(":".join(row) + "\n")