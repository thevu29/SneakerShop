import pyodbc

def Convert(item):
    array = []
    for i in range(0, len(item)):
        item[i] = str(item[i]).strip("'")
        array.append(item[i])
    return array

class AdUserData():
    def __init__(self):
        self.userList = []
        
        self.conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost;'
                      'Database=py_ql;'
                      'Trusted_Connection=yes;')
        
        data = self.conn.cursor()
        data.execute('select * from dbo.Customer')
        
        for item in data:
            item = Convert(item)
            if int(item[len(item) - 1]) == 1:
                self.userList.append(item)
            
    def getUserList(self):
        return self.userList
    
    def addUser(self, user):
        self.userList.append(user)
        
        add = self.conn.cursor()
        add.execute(f""" insert into dbo.Customer values
                        ('{user[0]}', N'{user[1]}', N'{user[2]}', '{user[3]}', N'{user[4]}', {user[5]}, {user[6]})
                    """)
        
        self.conn.commit()
        
    def deleteUser(self, user):
        self.userList.remove(user)
        
        delete = self.conn.cursor()
        delete.execute(f"update dbo.Customer set deleteStatus=0 where CustomerID = '{user[0]}'")
        
        self.conn.commit()
        
    def updateUserInfo(self, newUser):
        for user in self.userList:
            if user[0] == newUser[0]:
                self.userList.remove(user)
                self.userList.append(newUser)
        
        self.userList.sort(key=lambda x: x[0])
        
        update = self.conn.cursor()
        update.execute(f""" update dbo.Customer
                            set CustomerName = N'{newUser[1]}', CustomerAddress = N'{newUser[2]}', Phone = '{newUser[3]}', Gender = N'{newUser[4]}',
                                            Point = '{newUser[5]}'
                            where CustomerID = '{newUser[0]}'
                       """)
        
        self.conn.commit()