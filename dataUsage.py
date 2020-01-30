import csv
from decimal import Decimal
from dateutil.parser import parse

with open('LongFlow.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    first = True
    for row in reader:
        if not first:
            startTime = row[7]
            endTime = row[0]
            usage = float(row[5])
            print(row[0], usage, "\t",row[7])
                # time = startTime.split(' ')
                # print(startTime)
                # parsed = parse(startTime, fuzzy_with_tokens=True)
        else:
            first = False


# file = "LongFlow.csv"
#
# with open(file, 'r') as csv:
#     content = csv.read()
#
# print(content)
