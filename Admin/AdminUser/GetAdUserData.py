import pyodbc

def Convert(item):
    array = []
    for i in range(0, len(item)):
        item[i] = str(item[i]).strip("'")
        array.append(item[i])
    return array

class AdUserData():
    userList = []
    
    def __init__(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-P91166MQ\\THEVU_SQL;'
                      'Database=py_ql;'
                      'Trusted_Connection=yes;')

        data = conn.cursor()
        data.execute('select * from dbo.Customer')
        
        for item in data:
            item = Convert(item)
            self.userList.append(item)
            
    def getUserList(self):
        return self.userList