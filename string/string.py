def mySplit(s,ds):
    res = [s]
    for d in ds:
        t = []
        map(lambda x: t.extend(x.split(d)), res)
        res = t
    return [x for x in res if x]
s = 'asd;aad|dasd|dasd,sdasd|asd,,Adas|sdasd;Asdasd,d|asd'
result = mySplit(s, ';,|\t')
print(result)

import re
re.split('[,;\t|]+','asd;aad|dasd|dasd,sdasd|asd,,Adas|sdasd;Asdasd,d|asd')


