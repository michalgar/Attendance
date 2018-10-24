# import csv
# with open('C:\\Users\\Michal\\Documents\\test.csv', 'r') as csvfile:
#     content = csv.reader(csvfile, delimiter=',')
#     for row in content:
#         print(", ".join(row))
#
#
import csv
fields = ['first', 'second', 'third']
with open('C:\\Users\\Michal\\Documents\\test.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)