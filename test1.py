import pymysql
import re
db = pymysql.connect(
                    host='localhost',
                    port = 3306,
                    user = 'root',
                    password = '123456',
                    database = 'dict1',
                    charset = 'utf8'
                    )
sql = 'insert into word1 values(%s,%s)'
f = open('dict.txt','r')
cur = db.cursor()
#
# for i in f:
#     temp = i.split('  ', 1)
#     word = temp[0]
#     means = temp[1].strip()
#     print(word)
#     print(means)
#     cur.execute(sql,[word,means])
for line in f:
    # tmp = line.split(' ',1)
    # word = tmp[0]
    # mean = tmp[1].strip()
    # cur.execute(sql,[word,mean])

    tup = re.findall(r'(\S+)\s+(.*)',line)[0]
    cur.execute(sql, tup)
try:
    db.commit()
except:
    db.rollback()
cur.close()
db.close()