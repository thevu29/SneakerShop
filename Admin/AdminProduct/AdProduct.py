import pyodbc

def Convert(item):
    array = []
    for i in range(0, len(item)):
        item[i] = str(item[i]).strip("'")
        array.append(item[i])
    return array

class AdProductData():
    def __init__(self):
        self.productList = []
        self.imagePaths = []
        
        self.conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost;'
                      'Database=py_ql;'
                      'Trusted_Connection=yes;')

        self.loadDatabase()
        
    def loadDatabase(self):
        self.productList.clear()
        
        data = self.conn.cursor()
        data.execute('select * from dbo.Product')
       
        id = 1
        for item in data:
            item[2] = '{0:.2f}'.format(item[2]).rstrip('0').rstrip('.')
            
            imagePath = f'./img/product/SP{str(id).zfill(3)}.png'
            id += 1
            
            item = Convert(item)
            
            item.append(imagePath)
            self.productList.append(item)
            
    def getProductList(self):
        return self.productList
    
    def addProduct(self, product):
        self.productList.append(product)
        
        add = self.conn.cursor()
        add.execute(f"""insert into dbo.Product values
                        ('{product[0]}', '{product[1]}', {product[2]}, {product[3]}, '{product[4]}', '{product[5]}', '{product[6]}')
                    """)
        
        self.conn.commit()
        
    def deleteProduct(self, product):
        delete = self.conn.cursor()
        delete.execute(f"update dbo.Product set deleteStatus=0 where ProductID = '{product[0]}'")
        
        self.loadDatabase()
        self.conn.commit()
        
    def updateProductInfo(self, newProduct):
        for product in self.productList:
            if product[0] == newProduct[0]:
                self.productList.remove(product)
                self.productList.append(newProduct)
        
        self.productList.sort(key=lambda x: x[0])
        
        update = self.conn.cursor()
        update.execute(f""" update dbo.Product
                            set ProductName = '{newProduct[1]}', Price = '{newProduct[2]}', Quantity = '{newProduct[3]}', SupplierID = '{newProduct[4]}',
                                            CategoryID = '{newProduct[5]}'
                            where ProductID = '{newProduct[0]}'
                       """)
        
        self.conn.commit()