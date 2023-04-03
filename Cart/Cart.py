import pyodbc

def Convert(item):
    array = []
    for i in range(0, len(item)):
        item[i] = str(item[i]).strip("'")
        array.append(item[i])
    return array

class CartData():
    cartList = []
    
    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-P91166MQ\\THEVU_SQL;'
                      'Database=py_ql;'
                      'Trusted_Connection=yes;')
    
    def getCartList(self, accountId):
        self.cartList.clear()
        
        data = self.conn.cursor()
        data.execute(f"""select p.ProductID, p.ProductName, p.Price, c.SizeNumber, c.Quantity from Cart c JOIN Product p ON c.ProductID = p.ProductID 
                                where c.AccountID = '{accountId}'
                          """)
        
        for item in data:
            item[2] = '{0:.2f}'.format(item[2]).rstrip('0').rstrip('.')
            item = Convert(item)
            self.cartList.append(item)
                
        return self.cartList

    def addCart(self, quantity, size, accountId, productID):
        try:
            add = self.conn.cursor()
            add.execute(f"INSERT INTO Cart(Quantity, SizeNumber, AccountID, ProductID) VALUES({quantity}, {size}, '{accountId}', '{productID}')")
            
            self.conn.commit()
        except Exception as e:
            print(f"Error inserting values to database: {e}")
         
    def deleteCart(self, productID, accountId, size):
        delete = self.conn.cursor()
        delete.execute(f"DELETE FROM Cart WHERE ProductID ='{productID}' and AccountId = '{accountId}' and SizeNumber = '{size}'")
        
        self.conn.commit()
