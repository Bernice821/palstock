from flask import Flask,request
from flask_cors import CORS
import os,sys
sys.path.append(os.getcwd())
from sql import SQL

app=Flask(__name__)
CORS(app)
mysql=None
sqluser='root'
sqlpwd=''
sqldb=''
sqltable=''

@app.rosete("/api/indexStocks",methods=['POST'])
def updatIndex():
    mysql = SQL('127.0.0.1', sqluser, sqlpwd, sqldb, sqltable)
    try:
        sqlstr = f"`"
        query=SQL.inquery(mysql,sqlstr)[0][0]
            
        msg='success'
    except Exception as E:
        print(E)
        msg='error'
    mysql.close()
    return {'message':msg}, 200

if "__main__"==__name__:
    # mysql = SQL('127.0.0.1', sqluser, sqlpwd, sqldb, sqltable)
    app.run(host="0.0.0.0",port=12000)
    # getnew()
    # mysql.close()