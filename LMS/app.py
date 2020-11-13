import dbconn
import loadempmdm as emdm
#import loadloanmdm as lmdm
#import loaneng as le
import sys

args_list = sys.argv
print(args_list)
conn = None

conn = dbconn.getConn(args_list[2])

print(dbconn.g_conn_status)

#
if dbconn.g_conn_status == "active":
    if args_list[1].upper() == 'EMPDATA':
        LoadEmpObj = emdm.loadempmdm(conn,args_list[3])
        pass
#    elif args_list[1].upper() == 'LOANDATA':
#        LoadEmpObj = lmdm.loadempmdm(conn,args_list[3])
#        pass
#    elif args_list[1].upper() == 'PROCESSLOAN':
#        LoadEmpObj = le.loaneng(conn,args_list[3])
#        pass
else:
    print("*** Fatal Error getting DB Conn! ***")

# Run Modes
# ########################################################
# python app.py EMPDATA dbconfig.json appconfig.json
# python app.py LOANDATA dbconfig.json appconfig.json
# python app.py PROCESSLOAN dbconfig.json appconfig.json
