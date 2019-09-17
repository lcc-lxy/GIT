import pymysql
#建立数据库连接

db = pymysql.connect(host='localhost',
                     port = 3306,
                     user = 'root',
                     password ='123456',
                     database = 'dict',
                     charset = 'utf8'
                     )
#创建游标对象(操作数据库,执行sql语句,得到执行结果)
cur = db.cursor()
f = open('dict.txt','r')
# data = f.readlines()
# data = f.readlines()
id = 1
for item in f:

    tmp = item.split(' ',1)
    word = tmp[0]
    ex = tmp[1].strip()
    sql = "insert into words values (%s,%s,%s)"
    # print(sql)
    cur.execute(sql,[id,word,ex])
    id += 1
#游标方法

#提交到数据库
db.commit()
#关闭游标对象任务
cur.close()
#关闭数据库链接
db.close()