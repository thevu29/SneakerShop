import pyodbc

def Convert(item):
    array = []
    for i in range(0, len(item)):
        item[i] = str(item[i]).strip("'")
        array.append(item[i])
    return array

class ProductData():
    productList = []
    
    def __init__(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-P91166MQ\\THEVU_SQL;'
                      'Database=py_ql;'
                      'Trusted_Connection=yes;')
        self.data = conn.cursor()
        # self.data.execute('select * from Product')
    
    # ham lay so luong va size cua san pham dua vao ten san pham
    def getSizeAndQuantity(self, productName):
        arr = []
        self.data.execute("SELECT ps.SizeNumber,ps.Quantity FROM Product_Size ps JOIN Product p ON p.ProductID = ps.ProductID WHERE p.ProductName = " + "'" + productName + "'")
        for item in self.data:
            item = Convert(item)
            arr.append(item)
        return arr
    
    # ham lay toan bo san pham
    def getProductList(self,condition):
        listProduct = []
        if(condition.lower().capitalize() == "Tất cả"):
            self.data.execute("Select distinct p.ProductID,p.ProductName,p.Price from Product p JOIN Category c ON p.CategoryID = c.CategoryID " )
            for item in self.data:
                item = Convert(item)
                listProduct.append(item)
            return listProduct
        elif (condition.lower().capitalize() == "Nike"):
            self.data.execute("Select distinct p.ProductID,p.ProductName,p.Price from Product p JOIN Category c ON p.CategoryID = c.CategoryID WHERE c.CategoryName = " + "'" + condition + "'" )
            for item in self.data:
                item = Convert(item)
                listProduct.append(item)
            return listProduct
        elif (condition.lower().capitalize() == "Addidas"):
            self.data.execute("Select distinct p.ProductID,p.ProductName,p.Price from Product p JOIN Category c ON p.CategoryID = c.CategoryID WHERE c.CategoryName = " + "'" + condition + "'")
            for item in self.data:
                item = Convert(item)
                listProduct.append(item)
            return listProduct
        elif (condition.lower().capitalize() == "Balenciaga"):
            self.data.execute("Select distinct p.ProductID,p.ProductName,p.Price from Product p JOIN Category c ON p.CategoryID = c.CategoryID WHERE c.CategoryName = " + "'" + condition + "'")
            for item in self.data:
                item = Convert(item)
                listProduct.append(item)
            return listProduct
        elif (condition.lower().capitalize() == "Gucci"):
            self.data.execute("Select distinct p.ProductID,p.ProductName,p.Price from Product p JOIN Category c ON p.CategoryID = c.CategoryID WHERE c.CategoryName = " + "'" + condition + "'")
            for item in self.data:
                item = Convert(item)
                listProduct.append(item)
            return listProduct
        elif (condition.lower().capitalize() == "Vans"):
            self.data.execute("Select distinct p.ProductID,p.ProductName,p.Price from Product p JOIN Category c ON p.CategoryID = c.CategoryID WHERE c.CategoryName = " + "'" + condition + "'")
            for item in self.data:
                item = Convert(item)
                listProduct.append(item)
            return listProduct
    
        elif (condition.lower().capitalize() == "Converse"):
            self.data.execute("Select distinct p.ProductID,p.ProductName,p.Price from Product p JOIN Category c ON p.CategoryID = c.CategoryID WHERE c.CategoryName = " + "'" + condition + "'")
            for item in self.data:
                item = Convert(item)
                listProduct.append(item)
            return listProduct
        elif (condition.lower().capitalize() == "Jordan"):
            self.data.execute("Select distinct p.ProductID,p.ProductName,p.Price from Product p JOIN Category c ON p.CategoryID = c.CategoryID WHERE c.CategoryName = " + "'" + condition + "'")
            for item in self.data:
                item = Convert(item)
                listProduct.append(item)
            return listProduct
        elif (condition.lower().capitalize() == "Asics"):
            self.data.execute("Select distinct p.ProductID,p.ProductName,p.Price from Product p JOIN Category c ON p.CategoryID = c.CategoryID WHERE c.CategoryName = " + "'" + condition + "'")
            for item in self.data:
                item = Convert(item)
                listProduct.append(item)
            return listProduct
            
# obj = ProductData()
# print(obj.getProductList())