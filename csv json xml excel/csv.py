#!/use/bin/env python
# _*_ coding:utf-8 _*_
import csv
with open('pingan.csv', 'rb') as rf:
    reader = csv.reader(rf)
    with open('pingan2016.csv', 'wb') as wf:
        writer = csv.writer(wf)
        headers = reader.next()
        writer.writerow(headers)
        for row in reader:
            if row[0] < '2016-01-01':
                break
            if int(row[5]) >= 50000000:
                writer.writerow(row)