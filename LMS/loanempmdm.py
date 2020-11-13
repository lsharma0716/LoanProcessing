import json
import os
import csv

class loadempmdm:

    def __init__(self, i_conn, i_inputfile):
        self.conn = i_conn
 
        input_file = open(i_inputfile,"r")
        var_txt = input_file.read()
        input_file.close()
        json_data =  json.loads(var_txt)
        self.inputfile = json_data["EMPMDM"]
        self.LoanEmpData()


    def LoanEmpData(self):
        cursor = self.conn.cursor()
        l_stmt = """ insert into employees(
            empid,
            ename,
            branch,
            contact
        ) values({},"{}","{}","{}") """;

        with open(self.inputfile) as csvfile:
            reader = csv.DictReader(csvfile,delimiter=",")
            for row in reader:
                try:
                    print(row)
                    cursor.execute(l_stmt.format(row['Empid'],row['Name'],row['Branch'],row['Contact']))
                except Exception as e:
                    print(str(e))
            
        self.conn.commit()
        cursor.close()
        print('data loaded')    
