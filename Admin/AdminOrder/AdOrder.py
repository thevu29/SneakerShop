import pyodbc

class AdOrder():
    orderList = []
    
    def __init__(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-P91166MQ\\THEVU_SQL;'
                      'Database=py_ql;'
                      'Trusted_Connection=yes;')

        data = conn.cursor()
        data.execute('select * from dbo.CustomerOrder')
        
        for item in data:
            item[3] = '{0:.2f}'.format(item[3]).rstrip('0').rstrip('.')
            item = self.toString(item)
            self.orderList.append(item)
        
    def getOrderList(self):
        return self.orderList
    
    def toString(self, item):
        array = []
        for i in range(0, len(item)):
            item[i] = str(item[i].strip("'"))
            array.append(item[i])
        return array