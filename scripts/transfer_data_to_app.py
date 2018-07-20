'''
1. remote records of analyser/app/app.db's test_case table
2. query record from ./app.db's case_info 
3. insert them to test_case table
'''
import config
import sqlite3
from datetime import datetime

def main():
    # log start time
    start = datetime.now()

    tmp_db_path = config.db_path
    web_db_path = config.web_db

    tmp_conn = sqlite3.connect(tmp_db_path)
    web_conn = sqlite3.connect(web_db_path)

    tmp_c = tmp_conn.cursor()
    web_c = web_conn.cursor()

    # query case_info table
    tmp_c.execute('''select * from case_info''')
    ret = tmp_c.fetchall()
    print('query result: %s' % len(ret))
    tmp_conn.commit()
    tmp_conn.close()
    print('finish query records form case_info table')

    # delete records fo test_case table
    web_c.execute('delete from test_case')
    print('finish clean test_case table')

    # insert record to test_case table
    for sub in ret:
        sql = build_sql(sub)
        print('sql content: %s' %sql)
        web_c.execute(sql)

    web_conn.commit()
    web_conn.close();

    # log end time
    end = datetime.now()
    print('Time Comsume: %s' % (end - start).seconds)



# insert record into db
def build_sql(single):
    time_create = datetime.fromtimestamp(int(float(single[3]))).strftime("%Y-%m-%d %H:%M:%S.%f")
    time_update = datetime.fromtimestamp(int(float(single[5]))).strftime("%Y-%m-%d %H:%M:%S.%f")
    return "INSERT INTO TEST_CASE ('{}', '{}', '{}', '{}', '{}', '{}', '{}') VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')"\
    .format("id", "file_name", "author", "create_date", "last_update_by", "last_update_time", "file_path",\
        single[0], single[1], single[2], time_create, single[4], time_update, single[6])

''' test_case & case_info table sctructure
sqlite> .schema test_case
CREATE TABLE test_case (
    id INTEGER NOT NULL,
    file_name VARCHAR,
    author VARCHAR,
    create_date DATETIME,
    last_update_by VARCHAR,
    last_update_time DATETIME,
    file_path VARCHAR,
    PRIMARY KEY (id)
);

sqlite> .schema case_info
CREATE TABLE CASE_INFO(
ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
FILE_NAME TEXT NOT NULL,
AUTHOR TEXT NOT NULL,
CREATE_DATE TEXT NOT NULL,
LAST_UPDATE_BY TEXT NOT NULL,
LAST_UPDATE_TIME, FILE_PATH TEXT);
'''
if __name__ == '__main__':
    main()