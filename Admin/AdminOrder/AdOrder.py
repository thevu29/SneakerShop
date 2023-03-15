import pyodbc
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from AdminProduct import AdProduct

def Convert(item):
    array = []
    for i in range(0, len(item)):
        item[i] = str(item[i]).strip("'")
        array.append(item[i])
    return array

class AdOrderData():
    def __init__(self):
        self.orderList = []
        
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-P91166MQ\\THEVU_SQL;'
                      'Database=py_ql;'
                      'Trusted_Connection=yes;')

        data = conn.cursor()
        data.execute('select * from dbo.CustomerOrder')
        
        for item in data:
            item[3] = '{0:.2f}'.format(item[3]).rstrip('0').rstrip('.')
            item = Convert(item)
            self.orderList.append(item)
        
    def getOrderList(self):
        return self.orderList
    
class AdOrderDetailData():
    def __init__(self):
        self.orderDetailList = []
        
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-P91166MQ\\THEVU_SQL;'
                      'Database=py_ql;'
                      'Trusted_Connection=yes;')

        data = conn.cursor()
        data.execute('select * from dbo.OrderDetail')
        
        for item in data:
            item[3] = '{0:.2f}'.format(item[3]).rstrip('0').rstrip('.')
            item = Convert(item)
            
            self.orderDetailList.append(item)
    
    def getOrderList(self):
        return self.orderDetailList
    
    def getProductData(self):
        product = AdProduct.AdProductData()
        productList = product.getProductList()
        return productList        