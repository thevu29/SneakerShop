import pyodbc

def Convert(item):
    array = []
    for i in range(0, len(item)):
        item[i] = str(item[i]).strip("'")
        array.append(item[i])
    return array

class AdAccountData():    
    def __init__(self):
        self.accountList = []
        
        self.conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-P91166MQ\\THEVU_SQL;'
                      'Database=py_ql;'
                      'Trusted_Connection=yes;')
            
    def getAccountList(self):
        data = self.conn.cursor()
        data.execute('select * from dbo.Account')
        
        for item in data:
            item = Convert(item)
            self.accountList.append(item)
            
        return self.accountList
    
    def getCustomerIdOfAccount(self, accountId):
        customerID = self.conn.cursor()
        customerID.execute(f"select CustomerID from dbo.Account where AccountID = '{accountId}'")
        return customerID.fetchone()[0]
    
    def addAccount(self, account):
        self.accountList.append(account)
        
        add = self.conn.cursor()
        add.execute(f""" insert into dbo.Account values
                        ('{account[0]}', N'{account[1]}', N'{account[2]}', '{account[3]}', N'{account[4]}')
                    """)
        
        self.conn.commit()
        
    def deleteAccount(self, account):
        self.accountList.remove(account)
        
        delete = self.conn.cursor()
        delete.execute(f"delete from dbo.Account where AccountID = '{account[0]}'")
        
        self.conn.commit()
        
    def updateAccountInfo(self, newAccount):
        for account in self.accountList:
            if account[0] == newAccount[0]:
                self.accountList.remove(account)
                self.accountList.append(newAccount)
        
        self.accountList.sort(key=lambda x: x[0])
        
        update = self.conn.cursor()
        update.execute(f""" update dbo.Account
                            set Username = '{newAccount[1]}', Password = '{newAccount[2]}', AccessID = '{newAccount[3]}', CustomerID = '{newAccount[4]}'
                            where AccountID = '{newAccount[0]}'
                       """)
        
        self.conn.commit()
        
    def getAccountId(self, username):        
        data = self.conn.cursor()
        data.execute(f"select AccountId from dbo.Account where Username = '{username}'")
        
        accountId = ''
        for item in data:
            accountId = item[0]
            break
        
        return accountId