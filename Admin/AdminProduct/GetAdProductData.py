import pyodbc

def Convert(item):
    array = []
    for i in range(0, len(item)):
        item[i] = str(item[i]).strip("'")
        array.append(item[i])
    return array

class AdProductData():
    productList = []
    
    def __init__(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-P91166MQ\\THEVU_SQL;'
                      'Database=py_ql;'
                      'Trusted_Connection=yes;')

        data = conn.cursor()
        data.execute('select * from dbo.Product')
        
        for item in data:
            item[2] = '{0:.2f}'.format(item[2]).rstrip('0').rstrip('.')
            item = Convert(item)
            self.productList.append(item)
            
    def getProductList(self):
        return self.productList