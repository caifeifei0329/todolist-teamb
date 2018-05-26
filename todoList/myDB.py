import sqlite3
from datetime import datetime
import time


class TodoDB():
    # 添加用户
    def add_user(self, index, name, pwd):
        conn = sqlite3.connect('todolistDB.db')
        cursor = conn.cursor()
        try:
            cursor.execute("insert into user (id, username, userpwd) values (%d,\'%s\',\'%s\')" % (index, name, pwd))
            print("成功添加一个用户,id=%d,username=%s,userpwd=%s" % (index, name, pwd))
        except sqlite3.IntegrityError as e:
            print("id=%d 已存在，无法添加" % index)  # , type(e)
        cursor.close()
        conn.commit()
        conn.close()

    # 删除用户
    def delete_user(self, index):
        conn = sqlite3.connect('todolistDB.db')
        cursor = conn.cursor()
        cursor.execute("select id from user")
        c = [list(i) for i in cursor.fetchall()]
        try:
            if index in [x[0] for x in c]:
                cursor.execute("delete from user where id=%d" % (index))
                print("删除数据成功,id=", index)
            else:
                print("删除失败")
        except Exception as e:
            print(type(e))
        cursor.close()
        conn.commit()
        conn.close()

    # 更新用户
    def update_user(self, index, name):
        conn = sqlite3.connect('todolistDB.db')
        cursor = conn.cursor()
        cursor.execute("select id from user")
        c = [list(i) for i in cursor.fetchall()]
        # print(c)
        # lis=[{"id":x[0],"username":x[1],"userpwd":x[2]} for x in c]
        # print([d[0] for d in lis])
        try:
            if index in [x[0] for x in c]:
                # ***********************现在只能修改username 不能改pwd*********************************
                cursor.execute("update user set username=\'%s\' where id=%d" % (name, index))
                print("user表：id=%d 的数据被修改了,username=%s" % (index, name))
            else:
                print("id=%d 不在数据库user表中" % index)
        except Exception as e:
            print(type(e))
        cursor.close()
        conn.commit()
        conn.close()

    # 查找用户
    def select_user(self):
        conn = sqlite3.connect('todolistDB.db')
        cursor = conn.cursor()
        if not cursor.fetchall():
            cursor.execute("select * from user ")
            print("user表所有数据：", cursor.fetchall())
        else:
            return None
        cursor.close()
        conn.commit()
        conn.close()

    # 增加list
    def add_list(self, index, text, title):
        conn = sqlite3.connect('todolistDB.db')
        cursor = conn.cursor()
        try:
            cursor.execute("insert into list (id, content, title) values(%d,\'%s\', \'%s\')"%(index, text, title))
            print("成功写入一条数据content=%s" % text)
        except sqlite3.IntegrityError as e:
            print("id=%d 已存在，添加失败" % index)
        cursor.close()
        conn.commit()
        conn.close()

    # 删除list
    def delete_list(self, index):
        conn = sqlite3.connect('todolistDB.db')
        cursor = conn.cursor()
        cursor.execute("select id from list")
        c = [list(i) for i in cursor.fetchall()]
        try:
            if index in [x[0] for x in c]:
                cursor.execute("delete from list where id=%d" % index)
                print("id=%d 的数据已删除" % index)
            else:
                print("删除失败")
        except Exception as e:
            print(type(e))
        cursor.close()
        conn.commit()
        conn.close()

    # 修改list
    def update_list(slef, index, text):
        conn = sqlite3.connect('todolistDB.db')
        cursor = conn.cursor()
        c = [list(i) for i in cursor.fetchall()]
        try:
            if index in [x[0] for x in c]:
                cursor.execute("update list set content=\'%s\' where id=%d" % (text, index))
                print("list表：id=%s 的数据被修改了,content=%s" % (index, text))
            else:
                print("id=%d 不在数据库list表中" % index)
        except Exception as e:
            print(type(e))
        cursor.close()
        conn.commit()
        conn.close()

    # 查找list
    def select_list(slef):
        conn = sqlite3.connect('todolistDB.db')
        cursor = conn.cursor()
        if not cursor.fetchall():
            cursor.execute("select * from list ")
            print("list表所有数据：", cursor.fetchall())
        else:
            return None
        cursor.close()
        conn.commit()
        conn.close()


if __name__ == "__main__":
    # conn = sqlite3.connect('todolistDB.db')
    # cursor = conn.cursor()
    # cursor.execute("create table list(id INTEGER AUTO_INCREMENT,content varchar(500),time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,title varchar(100), primary key (id))")
    # cursor.execute("create table user (id INTEGER AUTO_INCREMENT, username varchar(20), userpwd varchar(30), primary key (id))")
    # cursor.execute("drop table list")
    # cursor.close()
    # conn.commit()
    # conn.close()

    myDb = TodoDB()
    # # myDb.add_user(1, 'zhangjing', '123456')
    # # myDb.delete_user(5)
    # # myDb.update_user(2,'lisi')

    # myDb.select_user()

    # index, text, title

    # myDb.add_list(2, "今天天气真好", "天气")
    # myDb.delete_list(2)
    # myDb.update_list(1, "今天把数据库完成了")
    myDb.select_list()
