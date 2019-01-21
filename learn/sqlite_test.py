import sqlite3

def save():
    # 链接到SQLite数据库，数据库文件是test.db如果文件不存在，会自动创建当前目录
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    # 执行一条SQL语句，创建user表
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    # 执行一条SQL语句，插入一条记录
    cursor.execute('insert into user (id, name) values (\'1\',\'Michael\')')

    cursor.rowcount
    cursor.close()

    conn.commit()
    conn.close()


def read():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    cursor.execute('select * from user where id=?', ('1',))

    values = cursor.fetchall()

    print(values)

    cursor.close()
    conn.close()


def main():
    read()


if __name__ == "__main__":
    main()