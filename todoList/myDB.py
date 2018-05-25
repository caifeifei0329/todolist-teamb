import sqlite3

conn = sqlite3.connect('todolistDB.db')
print("connect database")
cursor = conn.cursor()
# cursor.execute("create table list(id varchar(20) primary key,content varchar(500),time timestamp,title varchar(100))")
# cursor.execute("create table user (id varchar(20) primary key, username varchar(20), userpwd varchar(30))")
# cursor.execute("insert into user (id, username, userpwd) values (\'1\', \'zhangjing\', \'123456\')")
# cursor.execute("insert into list (id, content, time, title) values(\'2\',\'超速地回错哦阿基三颗星奥林\',\'2018-05-25\' , \'you guess\')")
cursor.execute("select * from list")

values = cursor.fetchall()
print(values)

cursor.close()
conn.commit()
conn.close()


# 添加用户
def add_user():
    cursor = conn.cursor()
    cursor.execute("insert into user (id, username, userpwd) values (\'1\', \'zhangjing\', \'123456\')")
    cursor.close()
    conn.commit()
    conn.close()


# 删除用户
def delete_user():
    cursor = conn.cursor()
    cursor.execute("delete from user where id=\'1\'")
    cursor.close()
    conn.commit()
    conn.close()


# 更新用户
def update_user():
    cursor = conn.cursor()
    cursor.execute("update user set username=\'cff\' where id=\'1\'")
    cursor.close()
    conn.commit()
    conn.close()


# 查找用户
def select_user():
    cursor = conn.cursor()
    cursor.execute("select * from user ")
    cursor.close()
    conn.commit()
    conn.close()


# 增加list
def add_list():
    cursor = conn.cursor()
    cursor.execute(
        "insert into list (id, content, time, title) values(\'2\',\'超速地回错哦阿基三颗星奥林\',\'2018-05-25\' , \'you guess\')")
    cursor.close()
    conn.commit()
    conn.close()


# 删除list
def delete_list():
    cursor = conn.cursor()
    cursor.execute("delete from list where id=\'1\'")
    cursor.close()
    conn.commit()
    conn.close()


# 修改list
def update_list():
    cursor = conn.cursor()
    cursor.execute("update list set content=\'cgishcbjkanckjskdgcuajcnalnckjsi\' where id=\'1\'")
    cursor.close()
    conn.commit()
    conn.close()


# 查找list
def select_list():
    cursor = conn.cursor()
    cursor.execute("select * from list ")
    cursor.close()
    conn.commit()
    conn.close()
