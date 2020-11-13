import os
import json
import pymysql
from pymysql.cursors import DictCursor

# g_conn_status = "inactive"

def readConfig(l_file_name):

    input_file = open(l_file_name,"r")
    var_txt = input_file.read()
    input_file.close()
    return json.loads(var_txt)

def getConn(l_file_name):
    
    global g_conn_status
    g_conn_status = "inactive"
    conn=""
    
    try:
        l_db_json = readConfig(l_file_name)
        print(l_db_json)
        conn = pymysql.connect(
            host = l_db_json["host"],
            port = l_db_json["port"],
            user = l_db_json["user"],
            password = l_db_json["password"],
            db = l_db_json["db"],
        )

    except Exception as e :
        print(str(e))
    else:
        g_conn_status = "active"
        print("Success")

    return conn        

if __name__ == "__main__":
    conn = getConn(l_file_name)
