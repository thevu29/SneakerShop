import pyodbc
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from AdminProduct import AdProduct
from AdminUser import AdUser

def Convert(item):
    array = []
    for i in range(0, len(item)):
        item[i] = str(item[i]).strip("'")
        array.append(item[i])
    return array

class AdOrderData():
    def __init__(self):
        self.orderList = []
        
        self.conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-P91166MQ\\THEVU_SQL;'
                      'Database=py_ql;'
                      'Trusted_Connection=yes;')

        data = self.conn.cursor()
        data.execute('select * from dbo.CustomerOrder')
        
        for item in data:
            item[2] = "-".join(str(item[2]).split('-')[::-1])
            item[3] = '{0:.2f}'.format(item[3]).rstrip('0').rstrip('.')
            item = Convert(item)
            self.orderList.append(item)
        
    def getOrderList(self):
        return self.orderList
    
    def addOrder(self, order):
        self.orderList.append(order)
        
        add = self.conn.cursor()
        add.execute(f"insert into dbo.CustomerOrder values ('{order[0]}', '{order[1]}', '{order[2]}', {order[3]}, N'{order[4]}')")
        
        self.conn.commit()
    
    def deleteOrder(self, order):
        self.orderList.remove(order)
        
        delete = self.conn.cursor()
        delete.execute(f"delete from dbo.CustomerOrder where OrderID = '{order[0]}'")
        
        self.conn.commit()
        
    def changeOrderStatus(self, changeOrder):
        for order in self.orderList:
            if order[0] == changeOrder[0]:
                self.orderList.remove(order)
                self.orderList.append(changeOrder)
                
        self.orderList.sort(key = lambda x: x[0])
        
        change = self.conn.cursor()
        change.execute(f""" update dbo.CustomerOrder
                            set OrderStatus = N'{changeOrder[4]}'
                            where OrderID = '{changeOrder[0]}'
                       """)
        
        self.conn.commit()
                
class AdOrderDetailData():
    def __init__(self):
        self.orderDetailList = []
        
        self.conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-P91166MQ\\THEVU_SQL;'
                      'Database=py_ql;'
                      'Trusted_Connection=yes;')

        data = self.conn.cursor()
        data.execute('select * from dbo.OrderDetail')
        
        for item in data:
            item[3] = '{0:.2f}'.format(item[3]).rstrip('0').rstrip('.')
            item = Convert(item)
            
            self.orderDetailList.append(item)
    
    def addOrderDetail(self, orderDetail):
        self.orderDetailList.append(orderDetail)
        
        add = self.conn.cursor()
        add.execute(f"insert into dbo.OrderDetail values ('{orderDetail[0]}', '{orderDetail[1]}', {orderDetail[2]}, {orderDetail[3]}, {orderDetail[4]})")
        
        self.conn.commit()
    
    def getOrderDetailList(self):
        return self.orderDetailList
    
    def getProductData(self):
        product = AdProduct.AdProductData()
        productList = product.getProductList()
        return productList        
    
    def getUserData(self):
        user = AdUser.AdUserData()
        userList = user.getUserList()
        return userList